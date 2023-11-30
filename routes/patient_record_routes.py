from flask import Blueprint, request

from constants.user_type import UserType
from controller.patient_record_controller import PatientRecordController
from utils.jwt_and_user_type_validator import jwt_and_user_type_required

blueprint = Blueprint('Patient Record Routes Blueprint', __name__)
patient_record_controller = PatientRecordController()


@blueprint.route('/create', methods=["POST"])
@jwt_and_user_type_required(UserType.DOCTOR)
def create_patient_record():
    return patient_record_controller.create_patient_record(request)


@blueprint.route('/<patient_record_id>/doctor/<doctor_id>', methods=["PATCH"])
@jwt_and_user_type_required(UserType.DOCTOR)
def update_patient_record(patient_record_id, doctor_id):
    return patient_record_controller.update_patient_record(patient_record_id, doctor_id, request)


@blueprint.route('/<patient_record_id>', methods=["GET"])
@jwt_and_user_type_required(UserType.DOCTOR)
def get_patient_record(patient_record_id):
    return patient_record_controller.get_patient_record(patient_record_id)


@blueprint.route('/patient/<patient_id>', methods=["GET"])
@jwt_and_user_type_required(UserType.DOCTOR)
def search_patient(patient_id):
    return patient_record_controller.get_patient_records_for_patient(patient_id)
