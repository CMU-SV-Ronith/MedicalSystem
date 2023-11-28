from entry.base_class import BaseClass


class PatientRecord(BaseClass):
    def __init__(self, _id, patient_id, appointment_id, content, doctor_id, min_heart_beat, max_heart_beat,
                 systolic_pressure, diastolic_pressure, time):
        super().__init__()
        self._id = _id
        self.patient_id = patient_id
        self.appointment_id = appointment_id
        self.content = content
        self.doctor_id = doctor_id
        self.min_heart_beat = min_heart_beat
        self.max_heart_beat = max_heart_beat
        self.systolic_pressure = systolic_pressure
        self.diastolic_pressure = diastolic_pressure
        self.time = time

    @classmethod
    def from_request_entry(cls, request_entry):
        return cls(
            _id=request_entry._id,
            patient_id=request_entry.patient_id,
            appointment_id=request_entry.appointment_id,
            content=request_entry.content,
            doctor_id=request_entry.doctor_id,
            min_heart_beat=request_entry.min_heart_beat,
            max_heart_beat=request_entry.max_heart_beat,
            systolic_pressure=request_entry.systolic_pressure,
            diastolic_pressure=request_entry.diastolic_pressure,
            time=request_entry.time
        )
