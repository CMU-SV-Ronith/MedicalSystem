class BaseResponse:
    def __init__(self, status_code, status_message, count, members: list):
        self.status_code = status_code
        self.status_message = status_message
        self.count = count
        # self.data = [member for member in members]
        self.data = members if members is not None else []

    def to_dict(self):
        return {
            "status_code": self.status_code,
            "status_message": self.status_message,
            "count": self.count,
            "data": [member.to_dict() if hasattr(member, 'to_dict') else member for member in self.data]
        }

    @classmethod
    def from_error_code(cls, base_status_response):
        return cls(base_status_response.value['status_code'], base_status_response.value['status_message'], 0, None)
