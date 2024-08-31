class NotFoundError(Exception):
    def __init__(self, notFound: str):
        super().__init__(notFound + " not found")


class AlreadyExistsError(Exception):
    def __init__(self, alreadyExists: str):
        super().__init__(alreadyExists + " already exists")
