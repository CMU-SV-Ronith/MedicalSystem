from entry.base_class import BaseClass
from request.doctor_review_request_entry import DoctorReviewRequestEntry


class DoctorReview(BaseClass):
    def __init__(self, _id, patient_id, doctor_id, rating: int, review: None, appointment_id):
        super().__init__()
        self._id = _id
        self.patient_id = patient_id
        self.rating = rating
        self.review = review
        self.doctor_id = doctor_id
        self.appointment_id = appointment_id

    @classmethod
    def from_request(cls, request_payload: DoctorReviewRequestEntry):
        return cls(
            _id=None,
            patient_id=request_payload.patient_id,
            doctor_id=request_payload.doctor_id,
            rating=request_payload.rating,
            review=request_payload.review,
            appointment_id=request_payload.appointment_id
        )
