import json

from entry.base_class import BaseClass


class Address(BaseClass):
    def __init__(self, _id, user_type, address_line_1, address_line_2, city, state, zip_code, country, user_id=None):
        super().__init__()
        self._id = _id
        self.user_id = user_id
        self.user_type = user_type
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    def to_json(self):
        return json.dumps({
            "id": self._id,
            "user_id": self.user_id,
            "user_type": self.user_type,
            "address_line_1": self.address_line_1,
            "address_line_2": self.address_line_2,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "country": self.country
        })

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(
            _id=json_dict["_id"],
            user_id=json_dict["user_id"],
            user_type=json_dict["user_type"],
            address_line_1=json_dict["address_line_1"],
            address_line_2=json_dict["address_line_2"],
            city=json_dict["city"],
            state=json_dict["state"],
            zip_code=json_dict["zip_code"],
            country=json_dict["country"]
        )

    @classmethod
    def from_request_entry(cls, request_entry):
        return cls(
            _id=None,  # Assuming the ID needs to be generated or is not provided.
            user_id=request_entry.user_id,
            user_type=request_entry.user_type,
            address_line_1=request_entry.address_line_1,
            address_line_2=request_entry.address_line_2,
            city=request_entry.city,
            state=request_entry.state,
            zip_code=request_entry.zip_code,
            country=request_entry.country
        )
