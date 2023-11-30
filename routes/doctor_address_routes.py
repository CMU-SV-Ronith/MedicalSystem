from flask import Blueprint, request

from constants.user_type import UserType
from controller.doctor_address_controller import DoctorAddressController
from utils.jwt_and_user_type_validator import jwt_and_user_type_required

blueprint = Blueprint('Doctor Address Routes Blueprint', __name__)

doctor_address_controller = DoctorAddressController()


# UPDATE: taking doctor id as path param
@blueprint.route('/<address_id>/doctor/<doctor_id>', methods=["PATCH"])
@jwt_and_user_type_required(UserType.DOCTOR)
def update_doctor_address(address_id, doctor_id):
    return doctor_address_controller.update_doctor_address(address_id, doctor_id, request)


# UPDATE: taking doctor id as path param
@blueprint.route('/<address_id>/doctor/<doctor_id>', methods=["GET"])
@jwt_and_user_type_required(UserType.DOCTOR)
def get_doctor_address(address_id, doctor_id):
    return doctor_address_controller.get_doctor_address(address_id, doctor_id)
