"""api"""
from fastapi import FastAPI, Response, Request, status
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from schemas.Conversation import Conversation, ConversationFull
from schemas.responses import CreatedResponse
from pydantic import ValidationError, error_wrappers
from beanie import init_beanie

app = FastAPI()


@app.on_event("startup")
async def init():
    # Create Motor client
    """initialises beanie"""
    print("initialising beanie...")
    client = AsyncIOMotorClient(
        "mongodb://root:example@localhost:27017/?authSource=admin&authMechanism=SCRAM-SHA-256"
    )
    await init_beanie(database=client.db_name, document_models=[Conversation, ConversationFull])


@app.post("/conversations", response_model=CreatedResponse, status_code=201)
async def create_conversation(convo: Conversation):
    """A Conversation describes a series of interactions with an LLM model. It 
        also contains the properties that will be used to send individual queries
        to the LLM. Chat queries will be anonymised and logged for audit 
        purposes"""
    try:
        obj = await convo.insert()
        return {"id": obj.to_json()["id"]}
    except Exception as e:
        return JSONResponse(content={"code": 500,
                                     "message": "Internal Server Error"},
                            status_code=500)


@app.get("/conversations")
async def get_conversations():
    """Retrieves all the conversations that a user has created, the conversation history is not provided here"""
    try:
        return await Conversation.find_all().to_list()
    except Exception as e:
        return JSONResponse(content={"code": 500,
                                     "message": "Internal Server Error"},
                            status_code=500)


@app.put("/conversations/{id}")
async def updates_conversation():
    """Allows the user to customise parameters and properties of a Conversation, thereby customising their experience"""
    return {"message": "Hello, World"}


@app.get("/conversations/{id}")
async def get_conversation_history():
    """Retrieves the entire conversation history with the LLM"""
    return {"message": "Hello, World"}


@app.delete("/conversations/{id}")
async def delete_conversation():
    """Deletes the entire conversation history with the LLM Model"""
    return {"message": "Hello, World"}


@app.post("/queries")
async def send_prompt_query():
    """This action sends a new Prompt query to the LLM and returns its response. If any errors occur when sending the prompt to the LLM, then a 422 error should be raised."""
    return {"message": "Hello, World"}


@app.exception_handler(RequestValidationError)
async def invalid_parameter_error(request: Request, exc: error_wrappers.ValidationError):
    """handles invalid parameters"""
    return JSONResponse(content={"code": 400, "message": "Invalid Parameters Provided"}, status_code=400)
