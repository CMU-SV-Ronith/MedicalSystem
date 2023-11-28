from dao.BaseDao import BaseDao
from entry.doctor_review import DoctorReview


class DoctorReviewDao(BaseDao):

    def __init__(self) -> None:
        self.collection_name = 'doctor_reviews'
        super().__init__(self.collection_name)

    def get_doctor_reviews(self, doctor_id):
        query = {'doctor_id': doctor_id}
        found_documents = super().search(query, None, None, None, None)

        result = []

        for document in found_documents:
            result.append(DoctorReview.from_dict(document))

        return result
