class Session:
    def __init__(self) -> None:
        self._email = None
        self._token = None
        self._expiry_time = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    @property
    def expiry_time(self):
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, value):
        self._expiry_time = value

    def to_dict(self):
        # return {k: v for k, v in self.__dict__.items() if v is not None and k != '_id'}
        return {k: v for k, v in self.__dict__.items() if v is not None}
