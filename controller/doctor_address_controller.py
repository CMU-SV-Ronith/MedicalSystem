from flask import make_response, jsonify

from Response.doctor_address_response import DoctorAddressResponse
from controller.base_controller import BaseController
from exception.erp_base_exception import ErpBaseException
from manager.doctor_address_manager import DoctorAddressManager
from manager.doctor_manager import DoctorManager
from request.doctor_request_entry import DoctorRequestEntry
from status_codes.error_status_code import ErrorStatusCode
from status_codes.success_status_code import SuccessStatusCode


class DoctorAddressController(BaseController):
    def __init__(self) -> None:
        self.doctor_address_manager = DoctorAddressManager()
        self.doctor_manager = DoctorManager()

    def update_doctor_address(self, address_id, doctor_id, request):
        try:
            request_payload = DoctorRequestEntry.from_request_ignore_user_type(request)
            self.doctor_manager.update_doctor(doctor_id, request_payload)
            doctor_address = self.doctor_address_manager.get_doctor_address(address_id, doctor_id)
            response = DoctorAddressResponse(SuccessStatusCode.DOCTOR_ADDRESS_UPDATE_SUCCESS, 1, [doctor_address])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = DoctorAddressResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = DoctorAddressResponse.of_error(ErrorStatusCode.DOCTOR_ADDRESS_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def get_doctor_address(self, address_id, doctor_id):
        try:
            doctor_address = self.doctor_address_manager.get_doctor_address(address_id, doctor_id)
            response = DoctorAddressResponse(SuccessStatusCode.DOCTOR_ADDRESS_RETRIEVAL_SUCCESS, 1, [doctor_address])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = DoctorAddressResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = DoctorAddressResponse.of_error(ErrorStatusCode.DOCTOR_ADDRESS_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)
