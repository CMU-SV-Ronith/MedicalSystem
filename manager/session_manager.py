from datetime import timedelta, datetime

from flask_jwt_extended import create_access_token

from constants.user_type import UserType
from entry.session import Session
from exception.invalid_payload_exception import InvalidPayloadException
from exception.resource_not_found_exception import ResourceNotFoundException
from manager.doctor_manager import DoctorManager
from manager.patient_manager import PatientManager
from request.session_request_entry import SessionRequestEntry
from status_codes.error_status_code import ErrorStatusCode


class SessionManager:

    def __init__(self) -> None:
        self.patient_manager = PatientManager()
        self.doctor_manager = DoctorManager()

    def create_session(self, session_request_entry: SessionRequestEntry) -> Session:
        self.validate_request_payload(session_request_entry)
        self.validate_user_credentials(session_request_entry)

        expires_delta = timedelta(seconds=900)
        expiry_time = datetime.now() + expires_delta

        additional_data = {'user_type': session_request_entry.user_type}

        token = create_access_token(identity=session_request_entry.email, expires_delta=expires_delta,
                                    additional_claims=additional_data)

        session = Session()
        session.email = session_request_entry.email
        session.token = token
        session.expiry_time = expiry_time

        return session

    def validate_request_payload(self, session_request_entry):
        if session_request_entry is None:
            raise InvalidPayloadException(ErrorStatusCode.SESSION_CREATE_FAILED,
                                          'Payload is invalid.')

        if session_request_entry.email is None or session_request_entry.email.strip() is None:
            raise InvalidPayloadException(ErrorStatusCode.SESSION_CREATE_FAILED,
                                          'Payload is invalid.')

        if session_request_entry.password is None or session_request_entry.password.strip() is None:
            raise InvalidPayloadException(ErrorStatusCode.SESSION_CREATE_FAILED,
                                          'Payload is invalid.')

        if session_request_entry.user_type is None or session_request_entry.user_type.strip() is None:
            raise InvalidPayloadException(ErrorStatusCode.SESSION_CREATE_FAILED,
                                          'Payload is invalid.')

    def validate_user_credentials(self, session_request_entry):
        base_class = None
        if session_request_entry.user_type.lower() == UserType.DOCTOR.name.lower():
            base_class = self.doctor_manager.get_doctor_by_credentials(session_request_entry.email,
                                                                       session_request_entry.password)
        elif session_request_entry.user_type.lower() == UserType.PATIENT.name.lower():
            base_class = self.patient_manager.get_patient_by_credentials(session_request_entry.email,
                                                                         session_request_entry.password)

        if base_class is None:
            raise ResourceNotFoundException(ErrorStatusCode.SESSION_CREATE_FAILED,
                                            'user not found with credentials')
