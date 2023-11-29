from dao.BaseDao import BaseDao
from entry.doctor import Doctor
from exception.resource_not_found_exception import ResourceNotFoundException
from status_codes.error_status_code import ErrorStatusCode


class DoctorDao(BaseDao):
    def __init__(self) -> None:
        self.collection_name = 'doctors'
        super().__init__(self.collection_name)

    def create_doctor(self, doctor):

        doctor = super().save(doctor)
        doctor.encoded_password = None

        return doctor

    def get_doctor(self, doctor_id):
        found_document = self.collection.find_one({'_id': doctor_id})

        if found_document is None:
            raise ResourceNotFoundException(ErrorStatusCode.DOCTOR_CREATION_FAILED,
                                            "Doctor does not exist with doctor id")

        doctor = Doctor.from_dict(found_document)
        doctor.encoded_password = None

        return doctor

    def search_doctor(self, request_payload, sort_by, sort_order, start, count):
        query = request_payload.to_dict()
        found_documents = super().search(query, sort_by, sort_order, start, count)

        if found_documents is None:
            raise Exception("Document not found")

        doctors = []
        for document in found_documents:
            doctors.append(Doctor.from_dict(document))

        return doctors

    def update_doctor(self, doctor_id, doctor):
        return super().update(doctor_id, doctor)

    def get_doctor_by_credentials(self, email, password):
        query = {'email': email, 'encoded_password': password}

        found_documents = super().search(query, None, None, None, None)

        if found_documents is None:
            raise Exception("Document not found")

        doctors = []
        for document in found_documents:
            doctors.append(Doctor.from_dict(document))

        return doctors
