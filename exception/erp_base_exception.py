class ErpBaseException(BaseException):
    def __init__(self, message, error_status_code, http_status_code) -> None:
        super().__init__(message)
        self.http_status_code = http_status_code
        self.error_status_code = error_status_code
