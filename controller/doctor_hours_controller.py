from flask import make_response, jsonify

from Response.doctor_hours_response import DoctorHoursResponse
from exception.erp_base_exception import ErpBaseException
from manager.doctor_hours_manager import DoctorHoursManager
from request.doctor_hours_request_entry import DoctorHoursRequestEntry
from status_codes.error_status_code import ErrorStatusCode
from status_codes.success_status_code import SuccessStatusCode


class DoctorHoursController:

    def __init__(self) -> None:
        self.doctor_hours_manager = DoctorHoursManager()

    def create_doctor_hour(self, doctor_id, request):
        try:
            request_payload = DoctorHoursRequestEntry.from_request(request)
            doctor_hour = self.doctor_hours_manager.create_doctor_hour(doctor_id, request_payload)
            response = DoctorHoursResponse(SuccessStatusCode.DOCTOR_CREATION_SUCCESS, [doctor_hour])
            return make_response(jsonify(response.to_dict()), 201)
        except ErpBaseException as e:
            response = DoctorHoursResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = DoctorHoursResponse.of_error(ErrorStatusCode.DOCTOR_CREATION_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def update_doctor_hour(self, doctor_id, doctor_hour_id, request):
        try:
            request_payload = DoctorHoursRequestEntry.from_request(request)
            doctor_hour = self.doctor_hours_manager.update_doctor_hour(doctor_id,doctor_hour_id,  request_payload)
            response = DoctorHoursResponse(SuccessStatusCode.DOCTOR_CREATION_SUCCESS, [doctor_hour])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = DoctorHoursResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = DoctorHoursResponse.of_error(ErrorStatusCode.DOCTOR_CREATION_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def get_doctor_hours(self, doctor_id):
        try:
            doctor_hours = self.doctor_hours_manager.get_doctor_hours(doctor_id)
            response = DoctorHoursResponse(SuccessStatusCode.DOCTOR_HOUR_RETRIEVAL_SUCCESS, doctor_hours)
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = DoctorHoursResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = DoctorHoursResponse.of_error(ErrorStatusCode.DOCTOR_HOUR_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def delete_doctor_hour(self, doctor_id, doctor_hour_id):
        try:
            doctor_hour = self.doctor_hours_manager.delete_doctor_hour(doctor_id, doctor_hour_id)
            response = DoctorHoursResponse(SuccessStatusCode.DOCTOR_HOUR_DELETION_SUCCESS, [doctor_hour])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = DoctorHoursResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = DoctorHoursResponse.of_error(ErrorStatusCode.DOCTOR_HOUR_DELETION_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)
