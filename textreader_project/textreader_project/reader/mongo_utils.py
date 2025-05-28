from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = "mongodb+srv://tusharkunwar993:gotchmall2058@cluster0.nne9ttn.mongodb.net/file_demo?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client["file_demo"]
