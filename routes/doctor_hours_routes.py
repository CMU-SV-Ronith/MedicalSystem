from flask import Blueprint, request

from constants.user_type import UserType
from controller.doctor_hours_controller import DoctorHoursController
from utils.jwt_and_user_type_validator import jwt_and_user_type_required

blueprint = Blueprint('Doctor Hours Blueprint', __name__)
doctor_hours_controller = DoctorHoursController()


@blueprint.route('/<doctor_id>/create', methods=["POST"])
@jwt_and_user_type_required(UserType.DOCTOR)
def create_doctor_hour(doctor_id):
    return doctor_hours_controller.create_doctor_hour(doctor_id, request)


@blueprint.route('/<doctor_id>/<doctor_hour_id>', methods=["PATCH"])
@jwt_and_user_type_required(UserType.DOCTOR)
def update_doctor_hour(doctor_id, doctor_hour_id):
    return doctor_hours_controller.update_doctor_hour(doctor_id, doctor_hour_id, request)


@blueprint.route('/<doctor_id>', methods=["GET"])
@jwt_and_user_type_required(UserType.PATIENT)
def get_doctor_hours(doctor_id):
    return doctor_hours_controller.get_doctor_hours(doctor_id)


@blueprint.route('/<doctor_id>/<doctor_hour_id>', methods=["DELETE"])
@jwt_and_user_type_required(UserType.DOCTOR)
def delete_doctor_hour(doctor_id, doctor_hour_id):
    return doctor_hours_controller.delete_doctor_hour(doctor_id, doctor_hour_id)
