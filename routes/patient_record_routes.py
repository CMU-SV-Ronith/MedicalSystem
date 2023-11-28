from flask import Blueprint, request

from controller.patient_record_controller import PatientRecordController

blueprint = Blueprint('Patient Record Routes Blueprint', __name__)
patient_record_controller = PatientRecordController()


@blueprint.route('/create', methods=["POST"])
def create_patient_record():
    return patient_record_controller.create_patient_record(request)


@blueprint.route('/<patient_record_id>/doctor/<doctor_id>', methods=["PATCH"])
def update_patient_record(patient_record_id, doctor_id):
    return patient_record_controller.update_patient_record(patient_record_id, doctor_id, request)


@blueprint.route('/<patient_record_id>', methods=["GET"])
def get_patient_record(patient_record_id):
    return patient_record_controller.get_patient_record(patient_record_id)


@blueprint.route('/patient/<patient_id>', methods=["GET"])
def search_patient(patient_id):
    return patient_record_controller.get_patient_records_for_patient(patient_id)
