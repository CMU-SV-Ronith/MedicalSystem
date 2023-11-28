class BaseClass:
    def __init__(self):
        self._id = None

    def to_dict(self):
        # return {k: v for k, v in self.__dict__.items() if v is not None and k != '_id'}
        return {k: v for k, v in self.__dict__.items() if v is not None}

    @classmethod
    def from_dict(cls, attributes_dict):
        return cls(**attributes_dict)

    def get_id(self):
        return self._id

    def set_id(self, _id):
        self._id = _id
