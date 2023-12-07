from flask import make_response, jsonify

from Response.doctor_response import DoctorResponse
from controller.base_controller import BaseController
from exception.erp_base_exception import ErpBaseException
from manager.doctor_manager import DoctorManager
from request.doctor_request_entry import DoctorRequestEntry
from status_codes.error_status_code import ErrorStatusCode
from status_codes.success_status_code import SuccessStatusCode


class DoctorController(BaseController):
    def __init__(self) -> None:
        self.doctor_manager = DoctorManager()

    def create_doctor(self, request):
        try:
            request_payload = DoctorRequestEntry.from_request(request)
            doctor = self.doctor_manager.create_doctor(request_payload)
            response = DoctorResponse(SuccessStatusCode.DOCTOR_CREATION_SUCCESS, 1, [doctor])
            return make_response(jsonify(response.to_dict()), 201)
        except ErpBaseException as e:
            response = DoctorResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = DoctorResponse.of_error(ErrorStatusCode.DOCTOR_CREATION_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def update_doctor(self, doctor_id, request):
        try:
            request_payload = DoctorRequestEntry.from_request_ignore_user_type(request)
            doctor = self.doctor_manager.update_doctor(doctor_id, request_payload)
            response = DoctorResponse(SuccessStatusCode.DOCTOR_UPDATE_SUCCESS, 1, [doctor])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = DoctorResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = DoctorResponse.of_error(ErrorStatusCode.DOCTOR_UPDATE_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def get_doctor(self, doctor_id):
        try:
            doctor = self.doctor_manager.get_doctor(doctor_id)
            response = DoctorResponse(SuccessStatusCode.RETRIEVED_DOCTOR_DATA_SUCCESS, 1, [doctor])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = DoctorResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = DoctorResponse.of_error(ErrorStatusCode.DOCTOR_DATA_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def search_doctor(self, request):
        try:
            sort_by, sort_order, start, count = self.extract_query_params()
            request_payload = DoctorRequestEntry.from_request_ignore_user_type(request)
            doctors = self.doctor_manager.search_doctor(request_payload, sort_by, sort_order, start, count)
            response = DoctorResponse(SuccessStatusCode.RETRIEVED_DOCTOR_DATA_SUCCESS, len(doctors), doctors)
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = DoctorResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = DoctorResponse.of_error(ErrorStatusCode.DOCTOR_DATA_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def get_doctor_and_doctor_hours(self, doctor_id):
        try:
            doctor = self.doctor_manager.get_doctor_and_doctor_hours(doctor_id)
            response = DoctorResponse(SuccessStatusCode.RETRIEVED_DOCTOR_DATA_SUCCESS, 1, [doctor])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = DoctorResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = DoctorResponse.of_error(ErrorStatusCode.DOCTOR_DATA_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)
