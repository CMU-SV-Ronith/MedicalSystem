from flask import Blueprint, request

from constants.user_type import UserType
from controller.prescription_controller import PrescriptionController
from utils.jwt_and_user_type_validator import jwt_and_user_type_required

blueprint = Blueprint('Prescription Routes Blueprint', __name__)
prescription_controller = PrescriptionController()


@blueprint.route('/create', methods=["POST"])
@jwt_and_user_type_required(UserType.DOCTOR)
def create_prescription():
    return prescription_controller.create_prescription(request)


@blueprint.route('/<prescription_id>/doctor/<doctor_id>', methods=["PATCH"])
@jwt_and_user_type_required(UserType.DOCTOR)
def update_prescription(prescription_id, doctor_id):
    return prescription_controller.update_prescription(prescription_id, doctor_id, request)


@blueprint.route('/<prescription_id>', methods=["GET"])
@jwt_and_user_type_required(UserType.DOCTOR)
def get_prescription(prescription_id):
    return prescription_controller.get_prescription(prescription_id)


@blueprint.route('/patient/<patient_id>', methods=["GET"])
@jwt_and_user_type_required(UserType.DOCTOR)
def search_prescription(patient_id):
    return prescription_controller.get_prescriptions_for_patient(patient_id)
