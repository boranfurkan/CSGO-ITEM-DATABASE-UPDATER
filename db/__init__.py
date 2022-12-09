from pymongo import MongoClient


class Database:
    def __init__(self, url, database_name, collection_name):
        self.url = url
        self.database_name = database_name
        self.collection_name = collection_name
        self.client = MongoClient(self.url)[self.database_name][self.collection_name]

    def get_all_items(self):
        return self.client.find()

    def get_one_item(self, item_name: str):
        if self.client.find({"name": item_name}):
            return self.client.find({"name": item_name})
        else:
            return "There is no matching item!"

    def create_or_update_item(self, document_array: list):
        for document in document_array:
            if self.client.find({"name": document["name"]}):
                self.client.replace_one({"name": document["name"]}, document, upsert=True)
        return "Create or update operation successfully completed!"

    def delete_item(self, item_name: str):
        if self.client.delete_one({"name": item_name}):
            return "Item successfully deleted"
        else:
            return "There is no matching item!"
