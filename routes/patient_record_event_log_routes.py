from flask import Blueprint

from constants.user_type import UserType
from controller.patient_record_event_log_controller import PatientRecordEventLogController
from utils.jwt_and_user_type_validator import jwt_and_user_type_required

blueprint = Blueprint('Patient Record Event Log Routes Blueprint', __name__)
patient_record_event_log_controller = PatientRecordEventLogController()


@blueprint.route('/<patient_record_id>')
@jwt_and_user_type_required(UserType.DOCTOR)
def get_patient_record_event_log(patient_record_id):
    return patient_record_event_log_controller.get_patient_record_event_log(patient_record_id)
