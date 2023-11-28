from flask import jsonify, make_response

from Response.doctor_rating_response import DoctorRatingResponse
from Response.doctor_review_response import DoctorReviewResponse
from exception.erp_base_exception import ErpBaseException
from manager.doctor_review_manager import DoctorReviewManager
from request.doctor_review_request_entry import DoctorReviewRequestEntry
from status_codes.error_status_code import ErrorStatusCode
from status_codes.success_status_code import SuccessStatusCode


class DoctorReviewController:
    def __init__(self):
        self.doctor_review_manager = DoctorReviewManager()

    def create_review(self, request):
        try:
            request_payload = DoctorReviewRequestEntry.from_request(request)

            doctor_review = self.doctor_review_manager.create_review(request_payload)
            response = DoctorReviewResponse(SuccessStatusCode.DOCTOR_REVIEW_CREATION_SUCCESS, [doctor_review])
            return make_response(jsonify(response.to_dict()), 201)
        except ErpBaseException as e:
            response = DoctorReviewResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = DoctorReviewResponse.of_error(ErrorStatusCode.DOCTOR_REVIEW_CREATION_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def get_doctor_rating(self, doctor_id):
        try:
            doctor_rating = self.doctor_review_manager.get_doctor_rating(doctor_id)
            response = DoctorRatingResponse(SuccessStatusCode.DOCTOR_RATING_RETRIEVAL_SUCCESS, [doctor_rating])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = DoctorRatingResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = DoctorRatingResponse.of_error(ErrorStatusCode.DOCTOR_RATING_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)
