from Response.base_response import BaseResponse


class PatientRecordResponse(BaseResponse):
    def __init__(self, base_status_response, count, members) -> None:
        super().__init__(base_status_response.value['status_code'], base_status_response.value['status_message'], count,
                         members)

    @classmethod
    def of_error(cls, base_status_response, message):
        return BaseResponse(base_status_response.value['status_code'], message, 0, None)
