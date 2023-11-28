from dao.BaseDao import BaseDao
from entry.doctor_hour import DoctorHour


class DoctorHoursDao(BaseDao):

    def __init__(self) -> None:
        self.collection_name = 'doctor_hours'
        super().__init__(self.collection_name)

    def create(self, doctor_hour):
        return super().save(doctor_hour)

    def get_doctor_hours_for_doctor(self, doctor_id):
        query = {'doctor_id': doctor_id}

        found_documents = super().search(query, None, None, None, None)

        doctor_hours = []
        for document in found_documents:
            doctor_hours.append(DoctorHour.from_dict(document))

        return doctor_hours
