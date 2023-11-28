from exception.erp_base_exception import ErpBaseException


class InvalidPayloadException(ErpBaseException):
    """Custom exception for invalid request entry validation errors."""

    def __init__(self, error_status_code, message):
        super().__init__("Invalid Payload: " + message, error_status_code, 400)
