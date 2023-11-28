from dao.BaseDao import BaseDao
from dao.database import get_database_instance
from entry.patient import Patient
from exception.resource_not_found_exception import ResourceNotFoundException
from status_codes.error_status_code import ErrorStatusCode


class PatientDao(BaseDao):
    def __init__(self) -> None:
        self.patient_collection = get_database_instance()["patients"]

    def create_patient(self, patient):
        patient.set_id(self.generate_id())
        inserted_id = self.patient_collection.insert_one(patient.to_dict()).inserted_id
        inserted_document = self.patient_collection.find_one({'_id': inserted_id})

        patient = Patient.from_dict(inserted_document)
        patient.encoded_password = None

        return patient

    def get_patient(self, patient_id):
        found_document = self.patient_collection.find_one({'_id': patient_id})

        if found_document is None:
            raise ResourceNotFoundException(ErrorStatusCode.PATIENT_CREATION_FAILED,
                                            "Patient does not exist with patient id")

        patient = Patient.from_dict(found_document)
        patient.encoded_password = None

        return patient

    def search_patient(self, request_payload):
        found_documents = self.patient_collection.find(request_payload.to_dict())

        if found_documents is None:
            raise Exception("Document not found")

        patients = []
        for document in found_documents:
            patients.append(Patient.from_dict(document))

        return patients

    def update_patient(self, patient_id, patient):
        self.patient_collection.update_one({'_id': patient_id}, {"$set": patient.to_dict()})

        updated_patient = self.patient_collection.find_one({'_id': patient_id})

        return Patient.from_dict(updated_patient)