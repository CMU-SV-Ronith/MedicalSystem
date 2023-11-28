from datetime import datetime



class DoctorHoursRequestEntry:
    def __init__(self, _id, doctor_id, day, start_time, end_time):
        self._id = _id
        self.doctor_id = doctor_id
        self.weekday = day
        self.start_time = start_time
        self.end_time = end_time

    @classmethod
    def from_request(cls, request):
        request_json = request.get_json(silent=True)
        return cls(
            _id=request_json.get('id'),
            doctor_id=request_json.get('doctor_id'),
            day=request_json.get('day'),
            start_time=request_json.get('start_time'),
            end_time=request_json.get('end_time')
        )
