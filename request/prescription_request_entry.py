class PrescriptionRequestEntry:
    def __init__(self, _id, patient_id, content, doctor_id, appointment_id, time):
        self._id = _id
        self.patient_id = patient_id
        self.content = content
        self.doctor_id = doctor_id
        self.appointment_id = appointment_id
        self.time = time

    @classmethod
    def from_request(cls, request):
        request = request.get_json(silent=True)
        return cls(
            _id=request.get('id'),
            patient_id=request.get('patient_id'),
            content=request.get('content'),
            doctor_id=request.get('doctor_id'),
            appointment_id=request.get('appointment_id'),
            time=request.get('time')
        )
