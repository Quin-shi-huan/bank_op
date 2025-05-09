class HttpBadRequest(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.status_code = 200
        self.name = "BadRequest"
        self.message = message
