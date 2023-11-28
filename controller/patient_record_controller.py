from flask import make_response, jsonify, Response

from Response.patient_record_response import PatientRecordResponse
from controller.base_controller import BaseController
from exception.erp_base_exception import ErpBaseException
from manager import patient_record_manager
from request.patient_record_request_entry import PatientRecordRequestEntry
from status_codes.error_status_code import ErrorStatusCode
from status_codes.success_status_code import SuccessStatusCode


class PatientRecordController(BaseController):

    def __init__(self) -> None:
        self.patient_record_manager = patient_record_manager.PatientRecordManager()

    def create_patient_record(self, request) -> Response:
        try:
            request_entry = PatientRecordRequestEntry.from_request(request)
            patient_record = self.patient_record_manager.create_patient_record(request_entry)
            response = PatientRecordResponse(SuccessStatusCode.PATIENT_RECORD_CREATION_SUCCESS, 1, [patient_record])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PatientRecordResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PatientRecordResponse.of_error(ErrorStatusCode.PATIENT_RECORD_CREATION_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def update_patient_record(self, patient_record_id, doctor_id, request):
        try:
            request_entry = PatientRecordRequestEntry.from_request(request)
            patient_record = self.patient_record_manager.update_patient_record(patient_record_id, doctor_id,
                                                                               request_entry)
            response = PatientRecordResponse(SuccessStatusCode.PATIENT_RECORD_CREATION_SUCCESS, 1, [patient_record])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PatientRecordResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PatientRecordResponse.of_error(ErrorStatusCode.PATIENT_RECORD_CREATION_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def get_patient_record(self, patient_record_id):
        try:
            patient_record = self.patient_record_manager.get_patient_record(patient_record_id)
            response = PatientRecordResponse(SuccessStatusCode.PATIENT_RECORD_CREATION_SUCCESS, 1, [patient_record])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PatientRecordResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PatientRecordResponse.of_error(ErrorStatusCode.PATIENT_RECORD_CREATION_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def get_patient_records_for_patient(self, patient_id):
        try:
            sort_by, sort_order, start, count = self.extract_query_params()
            patient_records = self.patient_record_manager.get_patient_records_for_patient(patient_id, sort_by,
                                                                                         sort_order,
                                                                                         start, count)
            response = PatientRecordResponse(SuccessStatusCode.PATIENT_RECORD_CREATION_SUCCESS, len(patient_records), patient_records)
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PatientRecordResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PatientRecordResponse.of_error(ErrorStatusCode.PATIENT_RECORD_CREATION_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)
