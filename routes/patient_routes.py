from flask import Blueprint, request

from controller.patient_controller import PatientController

blueprint = Blueprint('Patient Routes Blueprint', __name__)
patient_controller = PatientController()


@blueprint.route('/', methods=["POST"])
def create_patient():
    return patient_controller.create_patient(request)


@blueprint.route('/<patient_id>', methods=["PATCH"])
def update_patient(patient_id):
    return patient_controller.update_patient(patient_id, request)


@blueprint.route('/<patient_id>', methods=["GET"])
def get_patient(patient_id):
    return patient_controller.get_patient(patient_id)


@blueprint.route('/search', methods=["GET"])
def search_patient():
    return patient_controller.search_patient(request)
