from constants.patient_record_event_type import PatientRecordEventType
from dao import patient_record_dao
from entry.patient_record import PatientRecord
from exception.invalid_payload_exception import InvalidPayloadException
from manager.PatientRecordEventLogManager import PatientRecordEventLogManager
from request.patient_record_request_entry import PatientRecordRequestEntry
from status_codes.error_status_code import ErrorStatusCode


class PatientRecordManager:

    def __init__(self) -> None:
        self.patient_record_dao = patient_record_dao.PatientRecordDao()
        self.patient_record_event_log_manager = PatientRecordEventLogManager()

    def create_patient_record(self, request_entry):
        self.validate_create_payload(request_entry)
        patient_record = PatientRecord.from_request_entry(request_entry)
        patient_record = self.patient_record_dao.save_patient_record(patient_record)
        self.patient_record_event_log_manager.create_patient_record_event(patient_record.get_id(),
                                                                          patient_record.doctor_id,
                                                                          PatientRecordEventType.CREATE)
        return patient_record

    def update_patient_record(self, patient_record_id, doctor_id, request_entry):
        if request_entry is None:
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_RECORD_UPDATE_FAILED,
                                          "payload is invalid")

        patient_record = self.get_patient_record(patient_record_id)

        if patient_record.doctor_id != doctor_id:
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_RECORD_UPDATE_FAILED,
                                          "Patient record does not belong to doctor")

        update_patient_record_db_entry = self.update_patient_record_attributes(patient_record, request_entry)

        if update_patient_record_db_entry:
            patient_record = self.patient_record_dao.update_patient_record(patient_record_id, patient_record)
            self.patient_record_event_log_manager.create_patient_record_event(patient_record.get_id(),
                                                                              patient_record.doctor_id,
                                                                              PatientRecordEventType.UPDATE)

        return patient_record

    def get_patient_record(self, patient_record_id) -> PatientRecord:
        if patient_record_id is None:
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_RECORD_UPDATE_FAILED,
                                          "patient record id is invalid")

        return self.patient_record_dao.get_patient_record(patient_record_id)

    def get_patient_records_for_patient(self, patient_id, sort_by, sort_order, start, count) -> [PatientRecord]:
        if patient_id is None:
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_RECORD_UPDATE_FAILED,
                                          "patient id is invalid")

        return self.patient_record_dao.search_patient_records(patient_id, sort_by, sort_order, start, count)

    def validate_create_payload(self, request_entry):
        if not request_entry.patient_id or not request_entry.patient_id.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_RECORD_CREATION_FAILED,
                                          'Request contains an invalid patient id.')

        if not request_entry.appointment_id or not request_entry.appointment_id.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_RECORD_CREATION_FAILED,
                                          'Request contains an invalid appointment id.')

        if not request_entry.content or not request_entry.content.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_RECORD_CREATION_FAILED,
                                          'Request contains invalid content.')

        if not request_entry.doctor_id or not request_entry.doctor_id.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_RECORD_CREATION_FAILED,
                                          'Request contains an invalid doctor id.')

        if request_entry.min_heart_beat is None:
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_RECORD_CREATION_FAILED,
                                          'Request contains an invalid minimum heart beat.')

        if request_entry.max_heart_beat is None:
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_RECORD_CREATION_FAILED,
                                          'Request contains an invalid maximum heart beat.')

        if request_entry.systolic_pressure is None:
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_RECORD_CREATION_FAILED,
                                          'Request contains an invalid systolic pressure.')

        if request_entry.diastolic_pressure is None:
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_RECORD_CREATION_FAILED,
                                          'Request contains an invalid diastolic pressure.')

        if not request_entry.time:
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_RECORD_CREATION_FAILED,
                                          'Request contains an invalid time.')

    def update_patient_record_attributes(self, patient_record: PatientRecord,
                                         request_entry: PatientRecordRequestEntry) -> bool:
        update_db_entry = False

        if request_entry.content is not None:
            patient_record.content = request_entry.content
            update_db_entry = True

        if request_entry.min_heart_beat is not None:
            patient_record.min_heart_beat = request_entry.min_heart_beat
            update_db_entry = True

        if request_entry.max_heart_beat is not None:
            patient_record.max_heart_beat = request_entry.max_heart_beat
            update_db_entry = True

        if request_entry.systolic_pressure is not None:
            patient_record.systolic_pressure = request_entry.systolic_pressure
            update_db_entry = True

        if request_entry.diastolic_pressure is not None:
            patient_record.diastolic_pressure = request_entry.diastolic_pressure
            update_db_entry = True

        return update_db_entry
