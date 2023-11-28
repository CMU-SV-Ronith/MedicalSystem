class DoctorReviewRequestEntry:
    def __init__(self, patient_id, doctor_id, rating: int, review, appointment_id):
        self.patient_id = patient_id
        self.rating = rating
        self.review = review
        self.doctor_id = doctor_id
        self.appointment_id = appointment_id

    @classmethod
    def from_request(cls, request):
        request = request.get_json(silent=True)

        return cls(request.get('patient_id'), request.get('doctor_id'), request.get('rating'),
                   request.get('review'), request.get('appointment_id'))
