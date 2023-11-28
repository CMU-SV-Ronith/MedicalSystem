from flask import make_response, jsonify

from Response.prescription_response import PrescriptionResponse
from controller.base_controller import BaseController
from exception.erp_base_exception import ErpBaseException
from manager.prescription_manager import PrescriptionManager
from request.prescription_request_entry import PrescriptionRequestEntry
from status_codes.error_status_code import ErrorStatusCode
from status_codes.success_status_code import SuccessStatusCode


class PrescriptionController(BaseController):

    def __init__(self) -> None:
        self.prescription_manager = PrescriptionManager()

    def create_prescription(self, request):
        try:
            request_entry = PrescriptionRequestEntry.from_request(request)
            prescription = self.prescription_manager.create_prescription(request_entry)
            response = PrescriptionResponse(SuccessStatusCode.PRESCRIPTION_CREATION_SUCCESS, 1, [prescription])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PrescriptionResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PrescriptionResponse.of_error(ErrorStatusCode.PRESCRIPTION_CREATION_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def update_prescription(self, prescription_id, doctor_id, request):
        try:
            request_entry = PrescriptionRequestEntry.from_request(request)
            prescription = self.prescription_manager.update_prescription(prescription_id, doctor_id, request_entry)
            response = PrescriptionResponse(SuccessStatusCode.PRESCRIPTION_UPDATE_SUCCESS, 1, [prescription])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PrescriptionResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PrescriptionResponse.of_error(ErrorStatusCode.PRESCRIPTION_UPDATE_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def get_prescription(self, prescription_id):
        try:
            prescription = self.prescription_manager.get_prescription(prescription_id)
            response = PrescriptionResponse(SuccessStatusCode.PRESCRIPTION_RETRIEVAL_SUCCESS, 1, [prescription])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PrescriptionResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PrescriptionResponse.of_error(ErrorStatusCode.PRESCRIPTION_DATA_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def get_prescriptions_for_patient(self, patient_id):
        try:
            sort_by, sort_order, start, count = self.extract_query_params()
            patient_records = self.prescription_manager.get_prescriptions_for_patient(patient_id, sort_by,
                                                                                      sort_order,
                                                                                      start, count)
            response = PrescriptionResponse(SuccessStatusCode.PRESCRIPTION_RETRIEVAL_SUCCESS, len(patient_records),
                                            patient_records)
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PrescriptionResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PrescriptionResponse.of_error(ErrorStatusCode.PRESCRIPTION_DATA_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)
