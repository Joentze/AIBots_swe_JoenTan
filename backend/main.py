"""Backend API"""
import os
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from schemas.Conversation import Conversation, ConversationFull, ConversationList
from schemas.responses import CreatedResponse
from schemas.Prompt import Prompt
from pydantic import error_wrappers
from schemas.requests import ConversationPUT
from beanie import init_beanie
from handlers.mongo_handler import add_to_message_history
from handlers.openai_handler import get_completion
from anon.anonymiser import encrypt_prompt, decrypt_prompt
app = FastAPI()


@app.on_event("startup")
async def init():
    # Create Motor client
    """initialises beanie"""
    print("initialising beanie...")
    client = AsyncIOMotorClient(
        "mongodb://root:example@localhost:27017/?authSource=admin&authMechanism=SCRAM-SHA-256"
    )
    await init_beanie(database=client.db_name, document_models=[ConversationFull])


@app.post("/conversations", response_model=CreatedResponse, status_code=201)
async def create_conversation(convo: Conversation):
    """A Conversation describes a series of interactions with an LLM model. It 
        also contains the properties that will be used to send individual queries
        to the LLM. Chat queries will be anonymised and logged for audit 
        purposes"""
    try:
        convo_full = ConversationFull(**convo.to_json(), messages=[])
        obj = await convo_full.insert()
        return {"id": obj.to_json()["id"]}
    except Exception as e:
        print(e)
        return JSONResponse(content={"code": 500,
                                     "message": "Internal Server Error"},
                            status_code=500)


@app.get("/conversations", response_model=ConversationList)
async def get_conversations():
    """Retrieves all the conversations that a user has created, the conversation history is not provided here"""
    try:
        data = {"data": await ConversationFull.find_all().to_list()}
        return data
    except Exception as e:
        print(e)
        return JSONResponse(content={"code": 500,
                                     "message": "Internal Server Error"},
                            status_code=500)


@app.put("/conversations/{id}", status_code=204)
async def updates_conversation(id: str, convo: ConversationPUT):
    """Allows the user to customise parameters and properties of a Conversation, thereby customising their experience"""
    try:
        doc = await ConversationFull.get(id)
        await doc.set({ConversationFull.name: convo.name, ConversationFull.params: convo.params})
    except AttributeError:
        return JSONResponse(content={"code": 404,
                                     "message": "Specified resource(s) was not found"},
                            status_code=404)
    except Exception as e:
        print(e)
        return JSONResponse(content={"code": 500,
                                     "message": "Internal Server Error"},
                            status_code=500)


@app.get("/conversations/{id}", response_model=ConversationFull, status_code=200)
async def get_conversation_history(id: str):
    """Retrieves the entire conversation history with the LLM"""
    try:
        return await ConversationFull.get(id)

    except AttributeError:
        return JSONResponse(content={"code": 404,
                                     "message": "Specified resource(s) was not found"},
                            status_code=404)
    except Exception as e:
        print(e)
        return JSONResponse(content={"code": 500,
                                     "message": "Internal Server Error"},
                            status_code=500)


@app.delete("/conversations/{id}", status_code=200)
async def delete_conversation(id: str):
    """Deletes the entire conversation history with the LLM Model"""
    try:
        convo = await ConversationFull.get(id)
        await convo.delete()
    except AttributeError:
        return JSONResponse(content={"code": 404,
                                     "message": "Specified resource(s) was not found"},
                            status_code=404)
    except Exception as e:
        print(e)
        return JSONResponse(content={"code": 500,
                                     "message": "Internal Server Error"},
                            status_code=500)


@app.post("/queries", response_model=CreatedResponse, status_code=201)
async def send_prompt_query(id: str, prompt: Prompt):
    """This action sends a new Prompt query to the LLM and returns its response. If any errors occur when sending the prompt to the LLM, then a 422 error should be raised."""
    try:
        role, content = prompt.role, prompt.content

        doc = await ConversationFull.get(id)

        params = doc.params

        message_history = [decrypt_prompt(message.dict())
                           for message in doc.messages]
        print(message_history)
        encrypted_prompt = encrypt_prompt(prompt)

        print(encrypted_prompt)
        await add_to_message_history(id, encrypted_prompt)

        try:

            llm_response = await get_completion([*message_history, {"role": role, "content": content}], params={"model": "gpt-3.5-turbo", **params})

            message = await add_to_message_history(id, encrypt_prompt(llm_response))

            return {"id": message.to_json()["id"]}
        except Exception as e:
            print(e)
            return JSONResponse(content={"code": 422,
                                         "message": "Unable to create resource"},
                                status_code=422)
    except AttributeError as e:
        print(e)
        return JSONResponse(content={"code": 404,
                                     "message": "Specified resource(s) was not found"},
                            status_code=404)
    except Exception as e:
        print(e)
        return JSONResponse(content={"code": 500,
                                     "message": "Internal Server Error"},
                            status_code=500)


@app.exception_handler(RequestValidationError)
async def invalid_parameter_error(request: Request, exc: error_wrappers.ValidationError):
    """handles invalid parameters"""
    return JSONResponse(content={"code": 400, "message": "Invalid Parameters Provided"}, status_code=400)

if __name__ == "__main__":
    pass
