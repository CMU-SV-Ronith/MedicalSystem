from entry.base_class import BaseClass
from request.prescription_request_entry import PrescriptionRequestEntry


class Prescription(BaseClass):
    def __init__(self, _id, patient_id, content, doctor_id, appointment_id, time):
        super().__init__()
        self._id = _id
        self.patient_id = patient_id
        self.content = content
        self.doctor_id = doctor_id
        self.appointment_id = appointment_id
        self.time = time

    @classmethod
    def from_request_entry(cls, request_entry: PrescriptionRequestEntry):
        return cls(
            _id=request_entry._id,
            patient_id=request_entry.patient_id,
            appointment_id=request_entry.appointment_id,
            content=request_entry.content,
            doctor_id=request_entry.doctor_id,
            time=request_entry.time
        )
