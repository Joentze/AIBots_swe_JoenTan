from typing import Optional
import asyncio
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from schemas.Conversation import Conversation
from beanie import Document, Indexed, init_beanie


async def init():
    # Create Motor client
    client = AsyncIOMotorClient(
        "mongodb://root:example@localhost:27017/?authSource=admin&authMechanism=SCRAM-SHA-256"
    )

    # Init beanie with the Product document class
    await init_beanie(database=client.db_name, document_models=[Conversation])
    alls = await Conversation.find_all().to_list()
    print(alls)


if __name__ == "__main__":
    asyncio.run(init())
