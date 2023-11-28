from dao.doctor_review_dao import DoctorReviewDao
from entry.doctor_rating import DoctorRating
from entry.doctor_review import DoctorReview
from exception.erp_base_exception import ErpBaseException
from exception.invalid_payload_exception import InvalidPayloadException
from request.doctor_review_request_entry import DoctorReviewRequestEntry
from status_codes.error_status_code import ErrorStatusCode


class DoctorReviewManager:

    def __init__(self) -> None:
        self.doctor_review_dao = DoctorReviewDao()

    def create_review(self, request_payload: DoctorReviewRequestEntry) -> DoctorReview:
        self.validate_create_request(request_payload)
        try:
            doctor_review = DoctorReview.from_request(request_payload)
            return self.doctor_review_dao.save(doctor_review)
        except Exception as e:
            raise ErpBaseException(str(e), ErrorStatusCode.DOCTOR_REVIEW_CREATION_FAILED, 500)

    def get_doctor_rating(self, doctor_id):
        if doctor_id is None or doctor_id.strip() is None:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_REVIEW_CREATION_FAILED,
                                          'doctor id is invalid.')

        try:
            existing_reviews = self.doctor_review_dao.get_doctor_reviews(doctor_id)

            if len(existing_reviews) == 0:
                return DoctorRating(doctor_id, False)

            review_list = []
            rating = 0
            for review in existing_reviews:
                rating += review.rating
                if review.review is not None and review.review.strip() is not None:
                    review_list.append(review.review)

            rating /= len(existing_reviews)

            return DoctorRating(doctor_id, True, rating, review_list)
        except Exception as e:
            raise ErpBaseException(str(e), ErrorStatusCode.DOCTOR_REVIEW_CREATION_FAILED, 500)

    def validate_create_request(self, request_payload: DoctorReviewRequestEntry):
        if request_payload is None:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_REVIEW_CREATION_FAILED,
                                          'payload is invalid.')

        if request_payload.patient_id is None or request_payload.patient_id.strip() is None:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_REVIEW_CREATION_FAILED,
                                          'patient id is invalid.')

        if request_payload.doctor_id is None or request_payload.doctor_id.strip() is None:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_REVIEW_CREATION_FAILED,
                                          'doctor id is invalid.')

        if request_payload.rating is None or request_payload.rating < 0 or request_payload.rating > 5:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_REVIEW_CREATION_FAILED,
                                          'rating provided is invalid.')
