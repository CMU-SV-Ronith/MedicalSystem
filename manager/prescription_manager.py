from dao.prescription_dao import PrescriptionDao
from entry.prescription import Prescription
from exception.invalid_payload_exception import InvalidPayloadException
from request.prescription_request_entry import PrescriptionRequestEntry
from status_codes.error_status_code import ErrorStatusCode


class PrescriptionManager:

    def __init__(self) -> None:
        self.prescription_dao = PrescriptionDao()

    def create_prescription(self, request_entry: PrescriptionRequestEntry) -> Prescription:
        self.validate_create_payload(request_entry)

        prescription = Prescription.from_request_entry(request_entry)
        prescription = self.prescription_dao.create_prescription(prescription)

        return prescription

    def update_prescription(self, prescription_id, doctor_id, request_entry) -> Prescription:
        if request_entry is None:
            raise InvalidPayloadException(ErrorStatusCode.PRESCRIPTION_UPDATE_FAILED,
                                          "payload is invalid")

        prescription = self.get_prescription(prescription_id)

        if prescription.doctor_id != doctor_id:
            raise InvalidPayloadException(ErrorStatusCode.PRESCRIPTION_UPDATE_FAILED,
                                          "Prescription does not belong to doctor")

        update_patient_record_db_entry = self.update_prescription_attributes(prescription, request_entry)

        if update_patient_record_db_entry:
            prescription = self.prescription_dao.update_patient_record(prescription_id, prescription)

        return prescription

    def get_prescription(self, prescription_id) -> Prescription:
        if prescription_id is None:
            raise InvalidPayloadException(ErrorStatusCode.PRESCRIPTION_DATA_RETRIEVAL_FAILED,
                                          "prescription id is invalid")

        return self.prescription_dao.get_patient_record(prescription_id)

    def get_prescriptions_for_patient(self, prescription_id, sort_by, sort_order, start, count):
        if prescription_id is None:
            raise InvalidPayloadException(ErrorStatusCode.PRESCRIPTION_DATA_RETRIEVAL_FAILED,
                                          "prescription id is invalid")

        return self.prescription_dao.search_patient_records(prescription_id, sort_by, sort_order, start, count)

    def validate_create_payload(self, request_entry: PrescriptionRequestEntry):
        if not request_entry.patient_id or not request_entry.patient_id.strip():
            raise InvalidPayloadException(ErrorStatusCode.PRESCRIPTION_CREATION_FAILED,
                                          'Request contains an invalid patient id.')

        if not request_entry.appointment_id or not request_entry.appointment_id.strip():
            raise InvalidPayloadException(ErrorStatusCode.PRESCRIPTION_CREATION_FAILED,
                                          'Request contains an invalid appointment id.')

        if not request_entry.content or not request_entry.content.strip():
            raise InvalidPayloadException(ErrorStatusCode.PRESCRIPTION_CREATION_FAILED,
                                          'Request contains invalid content.')

        if not request_entry.doctor_id or not request_entry.doctor_id.strip():
            raise InvalidPayloadException(ErrorStatusCode.PRESCRIPTION_CREATION_FAILED,
                                          'Request contains an invalid doctor id.')

        if not request_entry.time:
            raise InvalidPayloadException(ErrorStatusCode.PRESCRIPTION_CREATION_FAILED,
                                          'Request contains an invalid time.')

    def update_prescription_attributes(self, prescription: Prescription,
                                       request_entry: PrescriptionRequestEntry) -> bool:
        update_db_entry = False

        if request_entry.content is not None:
            prescription.content = request_entry.content
            update_db_entry = True

        return update_db_entry
