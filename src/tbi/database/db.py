from pymongo import mongo_client
from pymongo.errors import ConnectionFailure
from tbi.database.config import settings
from tbi.core.logging import logger

try:
    client = mongo_client.MongoClient(settings.DATABASE_URL)
    logger.info("Connected to mongo database.")

    # Get database or create if doesn't exist
    database = client[settings.MONGO_INITDB_DATABASE]
except ConnectionFailure:
    logger.exception("Unable to connect to mongo database!")
