from flask import Blueprint, request

from constants.user_type import UserType
from controller.patient_controller import PatientController
from utils.jwt_and_user_type_validator import jwt_and_user_type_required

blueprint = Blueprint('Patient Routes Blueprint', __name__)
patient_controller = PatientController()


@jwt_and_user_type_required(UserType.PATIENT)
@blueprint.route('/', methods=["POST"])
def create_patient():
    return patient_controller.create_patient(request)


@jwt_and_user_type_required(UserType.PATIENT)
@blueprint.route('/<patient_id>', methods=["PATCH"])
def update_patient(patient_id):
    return patient_controller.update_patient(patient_id, request)


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/<patient_id>', methods=["GET"])
def get_patient(patient_id):
    return patient_controller.get_patient(patient_id)


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/search', methods=["GET"])
def search_patient():
    return patient_controller.search_patient(request)
