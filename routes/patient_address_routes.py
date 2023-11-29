from flask import Blueprint, request

from constants.user_type import UserType
from controller.patient_address_controller import PatientAddressController
from utils.jwt_and_user_type_validator import jwt_and_user_type_required

blueprint = Blueprint('Patient Address Routes Blueprint', __name__)

patient_address_controller = PatientAddressController()


# UPDATE: taking patient id as path param
@jwt_and_user_type_required(UserType.PATIENT)
@blueprint.route('/<address_id>/patient/<patient_id>', methods=["PATCH"])
def update_patient_address(address_id, patient_id):
    return patient_address_controller.update_patient_address(address_id, patient_id, request)


# UPDATE: taking patient id as path param
@jwt_and_user_type_required(UserType.PATIENT)
@blueprint.route('/<address_id>/patient/<patient_id>', methods=["GET"])
def get_patient_address(address_id, patient_id):
    return patient_address_controller.get_patient_address(address_id, patient_id)
