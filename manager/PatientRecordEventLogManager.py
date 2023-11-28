from datetime import datetime

from constants.patient_record_event_type import PatientRecordEventType
from dao.patient_record_event_log_dao import PatientRecordEventLogDao
from entry.patient_record_event_log import PatientRecordEventLog


class PatientRecordEventLogManager:
    def __init__(self):
        self.patient_record_event_log_dao = PatientRecordEventLogDao()

    def get_patient_record_event_log(self, patient_record_id):
        return self.patient_record_event_log_dao.get_patient_record_event_logs(patient_record_id)

    def create_patient_record_event(self, patient_record_id, doctor_id, event_type: PatientRecordEventType):
        event = PatientRecordEventLog(patient_record_id, event_type.value, doctor_id, datetime.now())
        self.patient_record_event_log_dao.save(event)
