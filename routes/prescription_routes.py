from flask import Blueprint, request

from constants.user_type import UserType
from controller.prescription_controller import PrescriptionController
from utils.jwt_and_user_type_validator import jwt_and_user_type_required

blueprint = Blueprint('Prescription Routes Blueprint', __name__)
prescription_controller = PrescriptionController()


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/create', methods=["POST"])
def create_prescription():
    return prescription_controller.create_prescription(request)


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/<prescription_id>/doctor/<doctor_id>', methods=["PATCH"])
def update_prescription(prescription_id, doctor_id):
    return prescription_controller.update_prescription(prescription_id, doctor_id, request)


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/<prescription_id>', methods=["GET"])
def get_prescription(prescription_id):
    return prescription_controller.get_prescription(prescription_id)


@jwt_and_user_type_required(UserType.DOCTOR)
@blueprint.route('/patient/<patient_id>', methods=["GET"])
def search_prescription(patient_id):
    return prescription_controller.get_prescriptions_for_patient(patient_id)
