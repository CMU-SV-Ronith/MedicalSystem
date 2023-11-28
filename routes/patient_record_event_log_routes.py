from flask import Blueprint

from controller.patient_record_event_log_controller import PatientRecordEventLogController

blueprint = Blueprint('Patient Record Event Log Routes Blueprint', __name__)
patient_record_event_log_controller = PatientRecordEventLogController()


@blueprint.route('/<patient_record_id>')
def get_patient_record_event_log(patient_record_id):
    return patient_record_event_log_controller.get_patient_record_event_log(patient_record_id)
