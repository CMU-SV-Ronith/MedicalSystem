import json
import datetime

from entry.base_class import BaseClass
from request.doctor_request_entry import DoctorRequestEntry


class Doctor(BaseClass):
    def __init__(self, _id, first_name, last_name, phone_number, email, encoded_password, encoded_ssn, npi, address_id
                 , region, insurance_number, insurance_provider, date_of_birth):
        super().__init__()
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.encoded_password = encoded_password
        self.encoded_ssn = encoded_ssn
        self.address_id = address_id
        self.insurance_number = insurance_number
        self.npi = npi
        self.region = region
        self.insurance_provider = insurance_provider

        if isinstance(date_of_birth, datetime.date) and not isinstance(date_of_birth, datetime.datetime):
            self.date_of_birth = datetime.datetime.combine(date_of_birth, datetime.time.min)
        else:
            self.date_of_birth = date_of_birth

    def to_json(self):
        return {
            "id": self._id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "email": self.email,
            "encoded_password": self.encoded_password,
            "encoded_ssn": self.encoded_ssn,
            "address_id": self.address_id,
            "insurance_number": self.insurance_number,
            "insurance_provider": self.insurance_provider,
            "date_of_birth": self.date_of_birth.isoformat() if self.date_of_birth else None
        }

    @classmethod
    def from_json(cls, json_dict):
        # Assuming the date_of_birth is provided as an ISO formatted date string
        date_of_birth = datetime.fromisoformat(json_dict["date_of_birth"]).date() if json_dict[
            "date_of_birth"] else None
        return cls(
            _id=json_dict["id"],
            first_name=json_dict["first_name"],
            last_name=json_dict["last_name"],
            phone_number=json_dict["phone_number"],
            email=json_dict["email"],
            encoded_password=json_dict["encoded_password"],
            encoded_ssn=json_dict["encoded_ssn"],
            address_id=json_dict["address_id"],
            insurance_number=json_dict["insurance_number"],
            insurance_provider=json_dict["insurance_provider"],
            date_of_birth=date_of_birth,
            npi=json_dict["npi"],
            region=json_dict["npi"]
        )

    @classmethod
    def from_doctor_request_entry(cls, doctor_request_entry: DoctorRequestEntry):
        return cls(
            _id=doctor_request_entry.id,
            first_name=doctor_request_entry.first_name,
            last_name=doctor_request_entry.last_name,
            phone_number=doctor_request_entry.phone_number,
            email=doctor_request_entry.email,
            encoded_password=doctor_request_entry.encoded_password,
            encoded_ssn=doctor_request_entry.encoded_ssn,
            address_id=doctor_request_entry.address_id,
            insurance_number=doctor_request_entry.insurance_number,
            insurance_provider=doctor_request_entry.insurance_provider,
            date_of_birth=doctor_request_entry.date_of_birth,
            npi=doctor_request_entry.npi,
            region=doctor_request_entry.city
        )
