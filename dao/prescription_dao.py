
from dao.base_dao import BaseDao
from entry.prescription import Prescription
from exception.resource_not_found_exception import ResourceNotFoundException
from status_codes.error_status_code import ErrorStatusCode


class PrescriptionDao(BaseDao):
    def __init__(self):
        self.collection_name = 'prescriptions'
        super().__init__(self.collection_name)

    def create_prescription(self, prescription):
        return super().save(prescription)

    def update_patient_record(self, prescription_id, prescription) -> Prescription:
        return super().update(prescription_id, prescription)

    def get_patient_record(self, prescription_id) -> Prescription:
        found_document = self.collection.find_one({'_id': prescription_id})

        if found_document is None:
            raise ResourceNotFoundException(ErrorStatusCode.PRESCRIPTION_DATA_RETRIEVAL_FAILED,
                                            "prescription does not exist with patient id")

        prescription = Prescription.from_dict(found_document)

        return prescription

    def search_patient_records(self, prescription_id, sort_by, sort_order, start, count):
        query = {"patient_id": prescription_id}
        documents = self.search(query, sort_by, sort_order, start, count)

        prescriptions = []

        for document in documents:
            prescriptions.append(Prescription.from_dict(document))

        return prescriptions
