from flask import make_response, jsonify

from Response.patient_address_response import PatientAddressResponse
from controller.base_controller import BaseController
from exception.erp_base_exception import ErpBaseException
from manager.patient_address_manager import PatientAddressManager
from request.patient_request_entry import PatientRequestEntry
from status_codes.error_status_code import ErrorStatusCode
from status_codes.success_status_code import SuccessStatusCode


class PatientAddressController(BaseController):
    def __init__(self) -> None:
        self.patient_address_manager = PatientAddressManager()

    def update_patient_address(self, address_id, patient_id, request):
        try:
            request_payload = PatientRequestEntry.from_request_ignore_user_type(request)
            patient_address = self.patient_address_manager.update_patient_address(address_id, patient_id, request_payload)
            response = PatientAddressResponse(SuccessStatusCode.PATIENT_ADDRESS_RETRIEVAL_SUCCESS, 1, [patient_address])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PatientAddressResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PatientAddressResponse.of_error(ErrorStatusCode.PATIENT_ADDRESS_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def get_patient_address(self, address_id, patient_id):
        try:
            patient_address = self.patient_address_manager.get_patient_address(address_id, patient_id)
            response = PatientAddressResponse(SuccessStatusCode.PATIENT_ADDRESS_RETRIEVAL_SUCCESS, 1, [patient_address])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PatientAddressResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PatientAddressResponse.of_error(ErrorStatusCode.PATIENT_ADDRESS_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)
