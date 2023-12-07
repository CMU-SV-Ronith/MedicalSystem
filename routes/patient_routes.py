from flask import Blueprint, request

from constants.user_type import UserType
from controller.patient_controller import PatientController
from utils.jwt_and_user_type_validator import jwt_and_user_type_required

blueprint = Blueprint('Patient Routes Blueprint', __name__)
patient_controller = PatientController()


@blueprint.route('/', methods=["POST"])
@jwt_and_user_type_required(UserType.PATIENT)
def create_patient():
    return patient_controller.create_patient(request)


@blueprint.route('/<patient_id>', methods=["PATCH"])
@jwt_and_user_type_required(UserType.PATIENT)
def update_patient(patient_id):
    return patient_controller.update_patient(patient_id, request)


@blueprint.route('/<patient_id>', methods=["GET"])
@jwt_and_user_type_required(UserType.DOCTOR)
def get_patient(patient_id):
    return patient_controller.get_patient(patient_id)


@blueprint.route('/search', methods=["GET"])
@jwt_and_user_type_required(UserType.DOCTOR)
def search_patient():
    return patient_controller.search_patient(request)

@blueprint.route('/getDetailedPatientInfo/<patient_id>', methods=["GET"])
@jwt_and_user_type_required(UserType.PATIENT)
def get_detailed_patient_info(patient_id):
    return patient_controller.get_detailed_patient_info(patient_id)