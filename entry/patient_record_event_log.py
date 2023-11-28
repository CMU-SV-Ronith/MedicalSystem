from datetime import datetime

from constants.patient_record_event_type import PatientRecordEventType
from entry.base_class import BaseClass


class PatientRecordEventLog(BaseClass):
    def __init__(self, patient_record_id, event_type, doctor_id, time, _id=None):
        super().__init__()
        self._id = _id
        self.patient_record_id = patient_record_id
        self.event_type = event_type
        self.doctor_id = doctor_id
        self.time = time
