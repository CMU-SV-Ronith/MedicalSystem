from flask import Blueprint, request

from constants.user_type import UserType
from controller.doctor_hours_controller import DoctorHoursController
from utils.jwt_and_user_type_validator import jwt_and_user_type_required

blueprint = Blueprint('Doctor Hours Blueprint', __name__)
doctor_hours_controller = DoctorHoursController()


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/<doctor_id>/create', methods=["POST"])
def create_doctor_hour(doctor_id):
    return doctor_hours_controller.create_doctor_hour(doctor_id, request)


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/<doctor_id>/<doctor_hour_id>', methods=["PATCH"])
def update_doctor_hour(doctor_id, doctor_hour_id):
    return doctor_hours_controller.update_doctor_hour(doctor_id, doctor_hour_id, request)


@jwt_and_user_type_required(UserType.PATIENT)
@blueprint.route('/<doctor_id>', methods=["GET"])
def get_doctor_hours(doctor_id):
    return doctor_hours_controller.get_doctor_hours(doctor_id)


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/<doctor_id>/<doctor_hour_id>', methods=["DELETE"])
def delete_doctor_hour(doctor_id, doctor_hour_id):
    return doctor_hours_controller.delete_doctor_hour(doctor_id, doctor_hour_id)
