from datetime import datetime

from dao.doctor_hours_dao import DoctorHoursDao
from entry.doctor_hour import DoctorHour
from exception.erp_base_exception import ErpBaseException
from exception.invalid_payload_exception import InvalidPayloadException
from request.doctor_hours_request_entry import DoctorHoursRequestEntry
from status_codes.error_status_code import ErrorStatusCode


class DoctorHoursManager:
    def __init__(self) -> None:
        self.doctor_hours_dao = DoctorHoursDao()

    def create_doctor_hour(self, doctor_id, request_payload: DoctorHoursRequestEntry):
        self.validate_create_payload(doctor_id, request_payload)
        doctor_hour = DoctorHour.from_request(request_payload)
        return self.doctor_hours_dao.create(doctor_hour)

    def validate_create_payload(self, doctor_id, request_payload: DoctorHoursRequestEntry):
        if doctor_id is None:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_HOUR_CREATION_FAILED,
                                          'doctor_id is invalid.')

        if request_payload is None:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_HOUR_CREATION_FAILED,
                                          'payload is invalid.')

        if request_payload.doctor_id is None or request_payload.doctor_id.strip() is None:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_HOUR_CREATION_FAILED,
                                          'doctor id is invalid in payload.')

        if doctor_id != request_payload.doctor_id:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_HOUR_CREATION_FAILED,
                                          'doctor id is incorrect in payload.')

        if request_payload.weekday is None:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_HOUR_CREATION_FAILED,
                                          'weekday is invalid in payload.')

        if request_payload.start_time is None or datetime.strptime(request_payload.start_time, '%H:%M').time() is None:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_HOUR_CREATION_FAILED,
                                          'start time is invalid in payload.')

        if request_payload.end_time is None or datetime.strptime(request_payload.end_time, '%H:%M').time() is None:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_HOUR_CREATION_FAILED,
                                          'end time is invalid in payload.')

    def get_doctor_hours(self, doctor_id):
        return self.doctor_hours_dao.get_doctor_hours_for_doctor(doctor_id)

    def delete_doctor_hour(self, doctor_id, doctor_hour_id):
        try:
            db_entry = self.doctor_hours_dao.find_by_id(doctor_hour_id, DoctorHour)

            if doctor_id != db_entry.doctor_id:
                raise Exception('doctor hour does not belong to doctor')

            self.doctor_hours_dao.delete_by_id(doctor_hour_id)
            return db_entry
        except Exception as e:
            raise ErpBaseException(str(e), ErrorStatusCode.DOCTOR_HOUR_DELETION_FAILED, 500)

    def update_doctor_hour(self, doctor_id, doctor_hour_id, request_payload):
        try:
            existing_entry = self.doctor_hours_dao.find_by_id(doctor_hour_id, DoctorHour)

            if doctor_id != existing_entry.doctor_id:
                raise Exception('doctor hour does not belong to doctor')

            self.update_fields_on_existing_entry(existing_entry, request_payload)
            return self.doctor_hours_dao.update(doctor_hour_id, existing_entry)

        except Exception as e:
            raise ErpBaseException(str(e), ErrorStatusCode.DOCTOR_HOUR_UPDATE_FAILED, 500)

    def update_fields_on_existing_entry(self, existing_entry: DoctorHour, request_payload: DoctorHoursRequestEntry):
        existing_entry.start_time = request_payload.start_time
        existing_entry.end_time = request_payload.end_time
