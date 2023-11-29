from dao.address_dao import AddressDao
from dao.patient_dao import PatientDao
from entry.address import Address
from entry.patient import Patient
from exception.invalid_payload_exception import InvalidPayloadException
from status_codes.error_status_code import ErrorStatusCode


class PatientManager:

    def __init__(self) -> None:
        self.patient_dao = PatientDao()
        self.address_dao = AddressDao()

    def create_patient(self, request_payload):
        self.validate_create_payload(request_payload)

        address = self.save_address(request_payload)
        patient = self.save_patient(address, request_payload)
        self.stamp_user_id_on_address(address, patient)

        return patient

    def stamp_user_id_on_address(self, address, patient):
        address.user_id = patient.get_id()
        self.address_dao.update_address(address.get_id(), address)

    def save_patient(self, address, request_payload):
        patient = Patient.from_patient_request_entry(request_payload)
        patient.address_id = address.get_id()
        patient = self.patient_dao.create_patient(patient)
        return patient

    def save_address(self, request_payload):
        address = Address.from_request_entry(request_payload)
        address = self.address_dao.create_address(address)
        return address

    def update_patient(self, patient_id, request_payload):
        patient = self.patient_dao.get_patient(patient_id)

        if patient is None:
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_UPDATE_FAILED,
                                          "Patient does not exist with id - " + patient_id)

        update_patient_db_entry = self.update_patient_attributes(patient, request_payload)

        if update_patient_db_entry:
            patient = self.patient_dao.update_patient(patient_id, patient)

        return patient

    def update_patient_attributes(self, patient, request_payload):
        update_patient_db_entry = False

        if request_payload.first_name and request_payload.first_name.strip():
            patient.first_name = request_payload.first_name
            update_patient_db_entry = True

        if request_payload.last_name and request_payload.last_name.strip():
            patient.last_name = request_payload.last_name
            update_patient_db_entry = True

        if request_payload.phone_number and request_payload.phone_number.strip():
            patient.phone_number = request_payload.phone_number
            update_patient_db_entry = True

        if request_payload.email and request_payload.email.strip():
            patient.email = request_payload.email
            update_patient_db_entry = True

        if request_payload.encoded_ssn and request_payload.encoded_ssn.strip():
            patient.encoded_ssn = request_payload.encoded_ssn
            update_patient_db_entry = True

        if request_payload.insurance_number and request_payload.insurance_number.strip():
            patient.insurance_number = request_payload.insurance_number
            update_patient_db_entry = True

        if request_payload.insurance_provider and request_payload.insurance_provider.strip():
            patient.insurance_provider = request_payload.insurance_provider
            update_patient_db_entry = True

        return update_patient_db_entry

    def get_patient(self, patient_id):
        return self.patient_dao.get_patient(patient_id).to_json()

    def search_patient(self, request_payload):
        return self.patient_dao.search_patient(request_payload)

    def validate_create_payload(self, request_payload):
        if not request_payload.first_name or not request_payload.first_name.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED,
                                          'Request contains an invalid first name.')

        if not request_payload.last_name or not request_payload.last_name.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED,
                                          'Request contains an invalid last name.')

        if not request_payload.phone_number or not request_payload.phone_number.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED,
                                          'Request contains an invalid phone number.')

        if not request_payload.email or not request_payload.email.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED,
                                          'Request contains an invalid email address.')

        # TODO: email regex validation

        if not request_payload.encoded_password or not request_payload.encoded_password.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED,
                                          'Request contains an invalid encoded password.')

        # TODO: Password complexity checks

        if not request_payload.encoded_ssn or not request_payload.encoded_ssn.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED,
                                          'Request contains an invalid encoded SSN.')

        if not request_payload.insurance_number or not request_payload.insurance_number.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED,
                                          'Request contains an invalid insurance number.')

        if not request_payload.insurance_provider or not request_payload.insurance_provider.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED,
                                          'Request contains an invalid insurance provider.')

        if not request_payload.date_of_birth:
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED,
                                          'Request contains an invalid date of birth.')

        if request_payload.user_type.lower() != 'patient':
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED, 'User type must be "patient".')

        if not request_payload.address_line_1 or not request_payload.address_line_1.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED,
                                          'Request contains an invalid address line 1.')

        if not request_payload.city or not request_payload.city.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED, 'Request contains an invalid city.')

        if not request_payload.state or not request_payload.state.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED, 'Request contains an invalid state.')

        if not request_payload.zip_code or not request_payload.zip_code.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED,
                                          'Request contains an invalid zip code.')

        if not request_payload.country or not request_payload.country.strip():
            raise InvalidPayloadException(ErrorStatusCode.PATIENT_CREATION_FAILED,
                                          'Request contains an invalid country.')

    def get_patient_by_credentials(self, email, password):
        return self.patient_dao.get_patient_by_credentials(email, password)
