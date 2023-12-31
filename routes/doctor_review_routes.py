from flask import Blueprint, request

from constants.user_type import UserType
from controller.doctor_review_controller import DoctorReviewController
from utils.jwt_and_user_type_validator import jwt_and_user_type_required

blueprint = Blueprint('Doctor Reviews Blueprint', __name__)
doctor_review_controller = DoctorReviewController()


@blueprint.route('/add', methods=["POST"])
@jwt_and_user_type_required(UserType.PATIENT)
def create_review():
    return doctor_review_controller.create_review(request)


@blueprint.route('/getRating/<doctor_id>', methods=["GET"])
@jwt_and_user_type_required(UserType.PATIENT)
def get_doctor_rating(doctor_id):
    return doctor_review_controller.get_doctor_rating(doctor_id)
