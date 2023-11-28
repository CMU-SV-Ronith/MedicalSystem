from flask import make_response, jsonify

from Response.patient_record_event_log_response import PatientRecordEventLogResponse
from Response.prescription_response import PrescriptionResponse
from controller.base_controller import BaseController
from exception.erp_base_exception import ErpBaseException
from manager.PatientRecordEventLogManager import PatientRecordEventLogManager
from status_codes.error_status_code import ErrorStatusCode
from status_codes.success_status_code import SuccessStatusCode


class PatientRecordEventLogController(BaseController):
    def __init__(self):
        self.patient_record_event_log_manager = PatientRecordEventLogManager()

    def get_patient_record_event_log(self, patient_record_id):
        try:
            event_logs = self.patient_record_event_log_manager.get_patient_record_event_log(patient_record_id)
            response = PatientRecordEventLogResponse(SuccessStatusCode.PRESCRIPTION_RETRIEVAL_SUCCESS, len(event_logs), event_logs)
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = PrescriptionResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = PrescriptionResponse.of_error(ErrorStatusCode.PATIENT_RECORD_EVENT_LOG_RETRIEVAL_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)
