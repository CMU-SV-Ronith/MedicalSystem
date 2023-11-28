import datetime

from entry.base_class import BaseClass
from request.doctor_hours_request_entry import DoctorHoursRequestEntry


class DoctorHour(BaseClass):

    def __init__(self, _id, doctor_id, weekday, start_time, end_time):
        super().__init__()
        self._id = _id
        self.doctor_id = doctor_id
        self.weekday = weekday
        self.start_time = start_time
        self.end_time = end_time

    @classmethod
    def from_request(cls, request_payload: DoctorHoursRequestEntry):
        return cls(request_payload._id, request_payload.doctor_id, request_payload.weekday, request_payload.start_time,
                   request_payload.end_time)
