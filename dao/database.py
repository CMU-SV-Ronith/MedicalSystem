from pymongo import MongoClient

mongo_database = None


def get_database_instance():
    global mongo_database

    if mongo_database is None:
        mongo_client = MongoClient()
        mongo_database = mongo_client["medical_management_service"]
    return mongo_database
