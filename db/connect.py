import os
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

MONGO_URI = os.environ.get("MONGO_URI")


def connect_database():
    client = MongoClient(MONGO_URI)
    return client['itemsDB']["items"]


def read_data():
    item_details = connect_database().find()
    for item in item_details:
        print(item)

read_data()