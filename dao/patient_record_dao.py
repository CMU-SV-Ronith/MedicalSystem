from pymongo import DESCENDING, ASCENDING

from dao import database
from dao.base_dao import BaseDao
from entry.patient_record import PatientRecord
from exception.resource_not_found_exception import ResourceNotFoundException
from status_codes.error_status_code import ErrorStatusCode


class PatientRecordDao(BaseDao):
    def __init__(self) -> None:
        self.collection_name = 'patient_records'
        super().__init__(self.collection_name)

    def save_patient_record(self, patient_record) -> PatientRecord:
        return super().save(patient_record)

    def update_patient_record(self, patient_record_id, patient_record):
        return super().update(patient_record_id, patient_record)

    def get_patient_record(self, patient_record_id):
        found_document = self.collection.find_one({'_id': patient_record_id})

        if found_document is None:
            raise ResourceNotFoundException(ErrorStatusCode.PATIENT_RECORD_DATA_RETRIEVAL_FAILED,
                                            "Patient does not exist with patient id")

        patient = PatientRecord.from_dict(found_document)

        return patient

    def search_patient_records(self, patient_id, sort_by, sort_order, start, count) -> [PatientRecord]:

        query = {"patient_id": patient_id}

        documents = self.search(query, sort_by, sort_order, start, count)

        patient_records = []

        for document in documents:
            patient_records.append(PatientRecord.from_dict(document))

        return patient_records
