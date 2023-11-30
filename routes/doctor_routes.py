from flask import Blueprint, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from constants.user_type import UserType
from controller.doctor_controller import DoctorController
from utils.jwt_and_user_type_validator import jwt_and_user_type_required
from utils.user_authentication import UserAuthentication

blueprint = Blueprint('Doctor Routes Blueprint', __name__)
doctor_controller = DoctorController()


@blueprint.route('/', methods=["POST"])
@jwt_and_user_type_required(UserType.DOCTOR)
def create_doctor():
    return doctor_controller.create_doctor(request)


@blueprint.route('/<doctor_id>', methods=["PATCH"])
@jwt_and_user_type_required(UserType.DOCTOR)
def update_doctor(doctor_id):
    return doctor_controller.update_doctor(doctor_id, request)


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/<doctor_id>', methods=["GET"])
def get_doctor(doctor_id):
    return doctor_controller.get_doctor(doctor_id)


@jwt_and_user_type_required(UserType.PATIENT)
@blueprint.route('/search', methods=["GET"])
def search_doctor():
    return doctor_controller.search_doctor(request)
