from flask import Blueprint, request

from controller.session_controller import SessionController

blueprint = Blueprint('Session Routes Blueprint', __name__)

session_controller = SessionController()


@blueprint.route('/create', methods=["POST"])
def create_session():
    return session_controller.create_session(request)

@blueprint.route('/delete', methods=["DELETE"])
def delete_session():
    return session_controller.delete_session()
