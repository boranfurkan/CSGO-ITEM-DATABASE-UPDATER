from db.db import Database
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME")

db = Database(MONGO_URI, DATABASE_NAME, COLLECTION_NAME)
