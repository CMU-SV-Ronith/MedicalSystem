from dao.address_dao import AddressDao
from exception.invalid_payload_exception import InvalidPayloadException
from status_codes.error_status_code import ErrorStatusCode


class DoctorAddressManager:

    def __init__(self) -> None:
        self.address_dao = AddressDao()

    def update_doctor_address(self, address_id, doctor_id, request_payload):
        address = self.get_doctor_address(address_id, doctor_id)

        update_address_db_entry = self.update_address_attributes(address, request_payload)

        if update_address_db_entry:
            self.address_dao.update_address(address.get_id(), address)

        return address

    def get_doctor_address(self, address_id, doctor_id):
        if not address_id and not address_id.strip():
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_ADDRESS_RETRIEVAL_FAILED, "address id is invalid.")

        address = self.address_dao.get_address_for_id(address_id)

        if address and address.user_id != doctor_id:
            raise InvalidPayloadException(ErrorStatusCode.DOCTOR_ADDRESS_RETRIEVAL_FAILED, "No address found.")

        return address

    def update_address_attributes(self, address, request_payload):
        update_address_db_entry = False

        if request_payload.address_line_1 and request_payload.address_line_1.strip():
            address.address_line_1 = request_payload.address_line_1
            update_address_db_entry = True

        if request_payload.address_line_2 and request_payload.address_line_2.strip():
            address.address_line_2 = request_payload.address_line_2
            update_address_db_entry = True

        if request_payload.city and request_payload.city.strip():
            address.city = request_payload.city
            update_address_db_entry = True

        if request_payload.state and request_payload.state.strip():
            address.state = request_payload.state
            update_address_db_entry = True

        if request_payload.zip_code and request_payload.zip_code.strip():
            address.zip_code = request_payload.zip_code
            update_address_db_entry = True

        if request_payload.country and request_payload.country.strip():
            address.country = request_payload.country
            update_address_db_entry = True

        return update_address_db_entry
