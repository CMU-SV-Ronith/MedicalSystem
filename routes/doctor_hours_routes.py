from flask import Blueprint, request

from controller.doctor_hours_controller import DoctorHoursController

blueprint = Blueprint('Doctor Hours Blueprint', __name__)
doctor_hours_controller = DoctorHoursController()


@blueprint.route('/<doctor_id>/create', methods=["POST"])
def create_doctor_hour(doctor_id):
    return doctor_hours_controller.create_doctor_hour(doctor_id, request)


@blueprint.route('/<doctor_id>/<doctor_hour_id>', methods=["PATCH"])
def update_doctor_hour(doctor_id, doctor_hour_id):
    return doctor_hours_controller.update_doctor_hour(doctor_id, doctor_hour_id, request)


@blueprint.route('/<doctor_id>', methods=["GET"])
def get_doctor_hours(doctor_id):
    return doctor_hours_controller.get_doctor_hours(doctor_id)


@blueprint.route('/<doctor_id>/<doctor_hour_id>', methods=["DELETE"])
def delete_doctor_hour(doctor_id, doctor_hour_id):
    return doctor_hours_controller.delete_doctor_hour(doctor_id, doctor_hour_id)
