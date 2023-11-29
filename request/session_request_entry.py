class SessionRequestEntry:
    def __init__(self, email, password, user_type) -> None:
        self.email = email
        self.password = password
        self.user_type = user_type

    @classmethod
    def from_request(cls, request):
        request = request.get_json(silent=True)
        return cls(request.get('email'), request.get('password'), request.get('user_type'))
