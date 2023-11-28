from dao.base_dao import BaseDao
from entry.patient_record_event_log import PatientRecordEventLog


class PatientRecordEventLogDao(BaseDao):
    def __init__(self):
        self.collection_name = 'patient_record_event_logs'
        super().__init__(self.collection_name)

    def get_patient_record_event_logs(self, patient_record_id):
        found_documents = self.collection.find({'patient_record_id': patient_record_id})

        event_logs = []

        for document in found_documents:
            event_logs.append(PatientRecordEventLog.from_dict(document))

        return event_logs
