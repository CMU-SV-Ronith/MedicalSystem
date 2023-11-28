from flask import Blueprint, request

from controller.doctor_review_controller import DoctorReviewController

blueprint = Blueprint('Doctor Reviews Blueprint', __name__)
doctor_review_controller = DoctorReviewController()


@blueprint.route('/add', methods=["POST"])
def create_review():
    return doctor_review_controller.create_review(request)


@blueprint.route('/getRating/<doctor_id>', methods=["GET"])
def get_doctor_rating(doctor_id):
    return doctor_review_controller.get_doctor_rating(doctor_id)
