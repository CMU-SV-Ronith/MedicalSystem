import json
import datetime

from entry.base_class import BaseClass


class Patient(BaseClass):
    def __init__(self, _id, first_name, last_name, phone_number, email, encoded_password, encoded_ssn, address_id,
                 insurance_number, insurance_provider, date_of_birth):
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
        self.insurance_provider = insurance_provider
        self.address = None

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
            date_of_birth=date_of_birth
        )

    @classmethod
    def from_patient_request_entry(cls, patient_entry):
        return cls(
            _id=patient_entry.id,
            first_name=patient_entry.first_name,
            last_name=patient_entry.last_name,
            phone_number=patient_entry.phone_number,
            email=patient_entry.email,
            encoded_password=patient_entry.encoded_password,
            encoded_ssn=patient_entry.encoded_ssn,
            address_id=patient_entry.address_id,
            insurance_number=patient_entry.insurance_number,
            insurance_provider=patient_entry.insurance_provider,
            date_of_birth=patient_entry.date_of_birth
        )
