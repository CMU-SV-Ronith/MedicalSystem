from flask import Blueprint, request

from constants.user_type import UserType
from controller.patient_record_controller import PatientRecordController
from utils.jwt_and_user_type_validator import jwt_and_user_type_required

blueprint = Blueprint('Patient Record Routes Blueprint', __name__)
patient_record_controller = PatientRecordController()


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/create', methods=["POST"])
def create_patient_record():
    return patient_record_controller.create_patient_record(request)


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/<patient_record_id>/doctor/<doctor_id>', methods=["PATCH"])
def update_patient_record(patient_record_id, doctor_id):
    return patient_record_controller.update_patient_record(patient_record_id, doctor_id, request)


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/<patient_record_id>', methods=["GET"])
def get_patient_record(patient_record_id):
    return patient_record_controller.get_patient_record(patient_record_id)


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/patient/<patient_id>', methods=["GET"])
def search_patient(patient_id):
    return patient_record_controller.get_patient_records_for_patient(patient_id)
