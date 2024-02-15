import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from schemas.Conversation import Conversation, ConversationFull
from beanie import init_beanie


async def init():
    # Create Motor client
    """initialises beanie"""
    client = AsyncIOMotorClient(
        "mongodb://root:example@localhost:27017/?authSource=admin&authMechanism=SCRAM-SHA-256"
    )
    # Init beanie with the Product document class
    await init_beanie(database=client.db_name, document_models=[Conversation, ConversationFull])
    # alls = await Conversation.find_all().to_list()
    # print(alls)


if __name__ == "__main__":
    asyncio.run(init())
