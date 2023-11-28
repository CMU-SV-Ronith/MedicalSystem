class PatientRecordRequestEntry:
    def __init__(self, _id, patient_id, appointment_id, content, doctor_id, min_heart_beat, max_heart_beat,
                 systolic_pressure, diastolic_pressure, time):
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
    def from_request(cls, request):
        request = request.get_json(silent=True)
        return cls(
            _id=request.get('id'),
            patient_id=request.get('patient_id'),
            appointment_id=request.get('appointment_id'),
            content=request.get('content'),
            doctor_id=request.get('doctor_id'),
            min_heart_beat=request.get('min_heart_beat'),
            max_heart_beat=request.get('max_heart_beat'),
            systolic_pressure=request.get('systolic_pressure'),
            diastolic_pressure=request.get('diastolic_pressure'),
            time=request.get('time')
        )
