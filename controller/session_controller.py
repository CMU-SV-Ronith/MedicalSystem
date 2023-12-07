from flask import make_response, jsonify

from Response.session_response import SessionResponse
from exception.erp_base_exception import ErpBaseException
from manager.session_manager import SessionManager
from request.session_request_entry import SessionRequestEntry
from status_codes.error_status_code import ErrorStatusCode
from status_codes.success_status_code import SuccessStatusCode


class SessionController:

    def __init__(self) -> None:
        self.session_manager = SessionManager()

    def create_session(self, request):
        try:
            session_request_entry = SessionRequestEntry.from_request(request)
            session = self.session_manager.create_session(session_request_entry)
            response = SessionResponse(SuccessStatusCode.SESSION_CREATE_SUCCESS, 1, [session])
            return make_response(jsonify(response.to_dict()), 200)
        except ErpBaseException as e:
            response = SessionResponse.of_error(e.error_status_code, str(e))
            return make_response(jsonify(response.to_dict()), e.http_status_code)
        except Exception as e:
            response = SessionResponse.of_error(ErrorStatusCode.SESSION_CREATE_FAILED, str(e))
            return make_response(jsonify(response.to_dict()), 500)

    def delete_session(self):
        response = SessionResponse(SuccessStatusCode.SESSION_DELETION_SUCCESS, 0, None)
        return make_response(jsonify(response.to_dict()), 200)
