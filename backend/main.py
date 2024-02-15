"""api"""
from fastapi import FastAPI

app = FastAPI()


@app.post("/conversations")
def create_conversation():
    """A Conversation describes a series of interactions with an LLM model. It 
        also contains the properties that will be used to send individual queries
        to the LLM. Chat queries will be anonymised and logged for audit 
        purposes"""
    return {"message": "Hello, World"}


@app.get("/conversations")
def get_conversations():
    """Retrieves all the conversations that a user has created, the conversation history is not provided here"""
    return {"message": "Hello, World"}


@app.put("/conversations/{id}")
def updates_conversation():
    """Allows the user to customise parameters and properties of a Conversation, thereby customising their experience"""
    return {"message": "Hello, World"}


@app.get("/conversations/{id}")
def get_conversation_history():
    """Retrieves the entire conversation history with the LLM"""
    return {"message": "Hello, World"}


@app.delete("/conversations/{id}")
def delete_conversation():
    """Deletes the entire conversation history with the LLM Model"""
    return {"message": "Hello, World"}


@app.post("/queries")
def send_prompt_query():
    """This action sends a new Prompt query to the LLM and returns its response. If any errors occur when sending the prompt to the LLM, then a 422 error should be raised."""
    return {"message": "Hello, World"}
