from flask import make_response, jsonify

from Response.patient_response import PatientResponse
from controller.base_controller import BaseController
from exception.erp_base_exception import ErpBaseException
from manager.patient_manager import PatientManager
from request.patient_request_entry import PatientRequestEntry
from status_codes.error_status_code import ErrorStatusCode
from status_codes.success_status_code import SuccessStatusCode


class PatientController(BaseController):
    def __init__(self) -> None:
        self.patient_manager = PatientManager()

    def create_patient(self, request):
        try:
            request_payload = PatientRequestEntry.from_request(request)
            patient = self.patient_manager.create_patient(request_payload)
            response = PatientResponse(SuccessStatusCode.PATIENT_CREATION_SUCCESS, 1, [patient])
            return make_response(jsonify(response.to_dict()), 201)
        except ErpBaseException as e:
            response = PatientResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PatientResponse.of_error(ErrorStatusCode.PATIENT_CREATION_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def update_patient(self, patient_id, request):
        try:
            request_payload = PatientRequestEntry.from_request_ignore_user_type(request)
            patient = self.patient_manager.update_patient(patient_id, request_payload)
            response = PatientResponse(SuccessStatusCode.PATIENT_UPDATE_SUCCESS, 1, [patient])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PatientResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PatientResponse.of_error(ErrorStatusCode.PATIENT_UPDATE_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def get_patient(self, patient_id):
        try:
            patient = self.patient_manager.get_patient(patient_id)
            response = PatientResponse(SuccessStatusCode.RETRIEVED_PATIENT_DATA_SUCCESS, 1, [patient])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PatientResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PatientResponse.of_error(ErrorStatusCode.PATIENT_DATA_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def search_patient(self, request):
        try:
            request_payload = PatientRequestEntry.from_request_ignore_user_type(request)
            patients = self.patient_manager.search_patient(request_payload)
            response = PatientResponse(SuccessStatusCode.RETRIEVED_PATIENT_DATA_SUCCESS, len(patients), patients)
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PatientResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PatientResponse.of_error(ErrorStatusCode.PATIENT_DATA_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def get_detailed_patient_info(self, patient_id):
        try:

            patient = self.patient_manager.get_detailed_patient_info(patient_id)
            response = PatientResponse(SuccessStatusCode.RETRIEVED_PATIENT_DATA_SUCCESS, 1, [patient])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PatientResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PatientResponse.of_error(ErrorStatusCode.PATIENT_DATA_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)
