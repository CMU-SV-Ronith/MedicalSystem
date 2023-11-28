import random
import string

from pymongo import ASCENDING, DESCENDING

from dao import database
from entry.base_class import BaseClass
from exception.resource_not_found_exception import ResourceNotFoundException


class BaseDao:
    def __init__(self, collection_name) -> None:
        self.collection = database.get_database_instance()[collection_name]

    @staticmethod
    def generate_id(length=18):
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

    def find_by_id(self, _id, class_type: type(BaseClass)):
        document = self.collection.find_one({'_id': _id})

        if document is None:
            raise ResourceNotFoundException("doctor hour not found with id: " + _id)

        return class_type.from_dict(document)

    def delete_by_id(self, _id):
        self.collection.delete_one({'_id': _id})
