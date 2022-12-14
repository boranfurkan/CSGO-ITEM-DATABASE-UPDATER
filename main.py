import os
import time
import asyncio
from logger import logger
from db.__init__ import Database
from dotenv import load_dotenv, find_dotenv
from components.__init__ import get_all_items, delete_all_dicts

load_dotenv(find_dotenv())
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME")


def main():
    while True:
        try:
            db = Database(MONGO_URI, DATABASE_NAME, COLLECTION_NAME)
            all_items = asyncio.run(get_all_items())
            db.create_or_update_item(all_items)
            logger.info("Successfully finished the loop.")
            time.sleep(1000)
            delete_dicts = delete_all_dicts()
            print(delete_dicts)
        except BaseException as error:
            logger.error(error)
            time.sleep(120)


if __name__ == "__main__":
    main()