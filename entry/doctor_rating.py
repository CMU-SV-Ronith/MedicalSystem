class DoctorRating:
    def __init__(self, doctor_id, rating_exists, rating=None, reviews=None):
        self.doctor_id = doctor_id
        self.rating_exists = rating_exists
        self.rating = rating
        self.reviews = reviews if reviews is not None else []


    def to_dict(self):
        # return {k: v for k, v in self.__dict__.items() if v is not None and k != '_id'}
        return {k: v for k, v in self.__dict__.items() if v is not None}