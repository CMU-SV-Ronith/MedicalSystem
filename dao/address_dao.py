import app
from dao.BaseDao import BaseDao
from dao.database import get_database_instance
from entry.address import Address


class AddressDao(BaseDao):
    def __init__(self) -> None:
        self.collection_name = 'addresses'
        super().__init__(self.collection_name)

    def create_address(self, address):
        return super().save(address)

    def get_address_for_id(self, address_id):
        return super().find_by_id(address_id, Address)

    def update_address(self, address_id, updated_address):
        self.collection.update_one({'_id': address_id}, {"$set": updated_address.to_dict()})

        updated_document = self.collection.find_one({'_id': address_id})

        return Address.from_dict(updated_document)
