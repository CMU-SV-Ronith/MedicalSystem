from dao.address_dao import AddressDao
from dao.doctor_dao import DoctorDao
from entry.address import Address
from entry.doctor import Doctor
from exception.invalid_payload_exception import InvalidPayloadException
from manager.doctor_address_manager import DoctorAddressManager
from manager.doctor_hours_manager import DoctorHoursManager
from status_codes.error_status_code import ErrorStatusCode


class DoctorManager:

    def __init__(self) -> None:
        self.doctor_dao = DoctorDao()
        self.address_dao = AddressDao()
        self.doctor_address_manager = DoctorAddressManager()
        self.doctor_hours_manager = DoctorHoursManager()

    def create_doctor(self, request_payload):
        self.validate_create_payload(request_payload)

        address = self.save_address(request_payload)
        doctor = self.save_doctor(address, request_payload)
        self.stamp_user_id_on_address(address, doctor)

        return doctor

    def stamp_user_id_on_address(self, address, doctor):
        address.user_id = doctor.get_id()
        self.address_dao.update_address(address.get_id(), address)

    def save_doctor(self, address, request_payload):
        doctor = Doctor.from_doctor_request_entry(request_payload)
        doctor.address_id = address.get_id()
        doctor = self.doctor_dao.create_doctor(doctor)
        return doctor

    def save_address(self, request_payload):
        address = Address.from_request_entry(request_payload)
        address = self.address_dao.create_address(address)
        return address

    def update_doctor(self, doctor_id, request_payload):
        doctor = self.doctor_dao.get_doctor(doctor_id)

        if doctor is None:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_UPDATE_FAILED,
                                          "Doctor does not exist with id - " + doctor_id)

        update_doctor_db_entry = self.update_doctor_attributes(doctor, request_payload)

        if update_doctor_db_entry:
            doctor = self.doctor_dao.update_doctor(doctor_id, doctor)

        self.doctor_address_manager.update_doctor_address(doctor.address_id, doctor_id, request_payload)

        return doctor

    def update_doctor_attributes(self, doctor, request_payload):
        update_doctor_db_entry = False

        if request_payload.first_name and request_payload.first_name.strip():
            doctor.first_name = request_payload.first_name
            update_doctor_db_entry = True

        if request_payload.last_name and request_payload.last_name.strip():
            doctor.last_name = request_payload.last_name
            update_doctor_db_entry = True

        if request_payload.phone_number and request_payload.phone_number.strip():
            doctor.phone_number = request_payload.phone_number
            update_doctor_db_entry = True

        if request_payload.email and request_payload.email.strip():
            doctor.email = request_payload.email
            update_doctor_db_entry = True

        if request_payload.encoded_ssn and request_payload.encoded_ssn.strip():
            doctor.encoded_ssn = request_payload.encoded_ssn
            update_doctor_db_entry = True

        if request_payload.insurance_number and request_payload.insurance_number.strip():
            doctor.insurance_number = request_payload.insurance_number
            update_doctor_db_entry = True

        if request_payload.insurance_provider and request_payload.insurance_provider.strip():
            doctor.insurance_provider = request_payload.insurance_provider
            update_doctor_db_entry = True

        if request_payload.city and request_payload.city.strip():
            doctor.region = request_payload.city
            update_doctor_db_entry = True

        return update_doctor_db_entry

    def get_doctor(self, doctor_id):
        return self.doctor_dao.get_doctor(doctor_id)

    def search_doctor(self, request_payload, sort_by, sort_order, start, count):
        return self.doctor_dao.search_doctor(request_payload, sort_by, sort_order, start, count)

    def validate_create_payload(self, request_payload):
        if not request_payload.first_name or not request_payload.first_name.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED,
                                          'Request contains an invalid first name.')

        if not request_payload.last_name or not request_payload.last_name.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED,
                                          'Request contains an invalid last name.')

        if not request_payload.phone_number or not request_payload.phone_number.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED,
                                          'Request contains an invalid phone number.')

        if not request_payload.email or not request_payload.email.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED,
                                          'Request contains an invalid email address.')

        # TODO: email regex validation

        if not request_payload.encoded_password or not request_payload.encoded_password.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED,
                                          'Request contains an invalid encoded password.')

        # TODO: Password complexity checks

        if not request_payload.encoded_ssn or not request_payload.encoded_ssn.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED,
                                          'Request contains an invalid encoded SSN.')

        if not request_payload.insurance_number or not request_payload.insurance_number.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED,
                                          'Request contains an invalid insurance number.')

        if not request_payload.insurance_provider or not request_payload.insurance_provider.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED,
                                          'Request contains an invalid insurance provider.')

        if not request_payload.date_of_birth:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED,
                                          'Request contains an invalid date of birth.')

        if request_payload.user_type.lower() != 'doctor':
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED, 'User type must be "doctor".')

        if not request_payload.address_line_1 or not request_payload.address_line_1.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED,
                                          'Request contains an invalid address line 1.')

        if not request_payload.city or not request_payload.city.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED, 'Request contains an invalid city.')

        if not request_payload.state or not request_payload.state.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED, 'Request contains an invalid state.')

        if not request_payload.zip_code or not request_payload.zip_code.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED,
                                          'Request contains an invalid zip code.')

        if not request_payload.country or not request_payload.country.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_CREATION_FAILED,
                                          'Request contains an invalid country.')

    def get_doctor_by_credentials(self, email, password):
        return self.doctor_dao.get_doctor_by_credentials(email, password)

    def get_doctor_and_doctor_hours(self, doctor_id) -> Doctor:
        doctor = self.doctor_dao.get_doctor(doctor_id)
        doctor.doctor_hours = self.doctor_hours_manager.get_doctor_hours(doctor_id)
        # [doctor_hour.to_json() for doctor_hour in self.doctor_hours_manager.get_doctor_hours(doctor_id)]

        return doctor
