from flask import request
from datetime import datetime

from entry.base_class import BaseClass


class DoctorRequestEntry(BaseClass):
    def __init__(self, id, user_id, user_type, first_name, last_name, phone_number, email,
                 encoded_password, encoded_ssn, npi, address_id, insurance_number,
                 insurance_provider, date_of_birth, address_line_1, address_line_2,
                 city, state, zip_code, country):
        self.id = id
        self.user_id = user_id
        self.user_type = user_type
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.encoded_password = encoded_password
        self.encoded_ssn = encoded_ssn
        self.address_id = address_id
        self.insurance_number = insurance_number
        self.insurance_provider = insurance_provider
        self.date_of_birth = date_of_birth  # Should be a datetime.date object
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.npi = npi
        self.region = city

    @classmethod
    def from_request(cls, request):
        request_json = request.get_json(silent=True)
        return cls(
            id=request_json.get('id'),
            user_id=request_json.get('user_id'),
            user_type=request_json.get('user_type', 'doctor'),
            first_name=request_json.get('first_name'),
            last_name=request_json.get('last_name'),
            phone_number=request_json.get('phone_number'),
            email=request_json.get('email'),
            encoded_password=request_json.get('encoded_password'),
            encoded_ssn=request_json.get('encoded_ssn'),
            address_id=request_json.get('address_id'),
            insurance_number=request_json.get('insurance_number'),
            insurance_provider=request_json.get('insurance_provider'),
            date_of_birth=datetime.fromisoformat(request_json.get('date_of_birth')).date() if request_json.get(
                'date_of_birth') else None,
            address_line_1=request_json.get('address_line_1'),
            address_line_2=request_json.get('address_line_2'),
            city=request_json.get('city'),
            state=request_json.get('state'),
            zip_code=request_json.get('zip_code'),
            country=request_json.get('country'),
            npi=request_json.get('npi')
        )

    @classmethod
    def from_request_ignore_user_type(cls, request):
        payload = DoctorRequestEntry.from_request(request)
        payload.user_type = None

        return payload
