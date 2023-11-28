import random
import string

from pymongo import ASCENDING, DESCENDING

from dao import database
from entry.base_class import BaseClass


class BaseDao:
    def __init__(self, collection_name) -> None:
        self.collection = database.get_database_instance()[collection_name]

    @staticmethod
    def generate_id(length=28):
        characters = string.ascii_lowercase + string.digits
        random_string = ''.join(random.choice(characters) for i in range(length))
        return random_string

    def save(self, instance: BaseClass):
        class_type = type(instance)

        instance.set_id(self.generate_id())

        inserted_id = self.collection.insert_one(instance.to_dict()).inserted_id
        inserted_document = self.collection.find_one({'_id': inserted_id})

        return class_type.from_dict(inserted_document)

    def update(self, base_class_id, instance: BaseClass):
        class_type = type(instance)

        self.collection.update_one({'_id': base_class_id}, {"$set": instance.to_dict()})
        updated_document = self.collection.find_one({'_id': base_class_id})

        return class_type.from_dict(updated_document)

    def search(self, query, sort_by, sort_order, start, count):
        order = DESCENDING if sort_order is not None and sort_order.lower() == 'desc' else ASCENDING
        documents = self.collection.find(query)

        if sort_by:
            documents = documents.sort(sort_by, order)
        if start:
            documents = documents.skip(start)
        if count:
            documents = documents.limit(count)

        return documents
