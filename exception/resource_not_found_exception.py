from exception.erp_base_exception import ErpBaseException


class ResourceNotFoundException(ErpBaseException):

    def __init__(self, error_status_code, message):
        super().__init__("Resource Not Found: " + message, error_status_code, 404)
