from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = ""
    client = MongoClient(CONNECTION_STRING)
    return client["file_demo"]
