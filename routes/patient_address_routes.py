from flask import Blueprint, request

from controller.patient_address_controller import PatientAddressController

blueprint = Blueprint('Patient Address Routes Blueprint', __name__)

patient_address_controller = PatientAddressController()


# UPDATE: taking patient id as path param
@blueprint.route('/<address_id>/patient/<patient_id>', methods=["PATCH"])
def update_patient_address(address_id, patient_id):
    return patient_address_controller.update_patient_address(address_id, patient_id, request)


# UPDATE: taking patient id as path param
@blueprint.route('/<address_id>/patient/<patient_id>', methods=["GET"])
def get_patient_address(address_id, patient_id):
    return patient_address_controller.get_patient_address(address_id, patient_id)
