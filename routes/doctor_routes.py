from flask import Blueprint, request

from controller.doctor_controller import DoctorController

blueprint = Blueprint('Doctor Routes Blueprint', __name__)
doctor_controller = DoctorController()


@blueprint.route('/', methods=["POST"])
def create_doctor():
    return doctor_controller.create_doctor(request)


@blueprint.route('/<doctor_id>', methods=["PATCH"])
def update_doctor(doctor_id):
    return doctor_controller.update_doctor(doctor_id, request)


@blueprint.route('/<doctor_id>', methods=["GET"])
def get_doctor(doctor_id):
    return doctor_controller.get_doctor(doctor_id)


@blueprint.route('/search', methods=["GET"])
def search_doctor():
    return doctor_controller.search_doctor(request)
