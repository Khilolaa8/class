import uuid


class Pupil:
    def __init__(self, name, fam):
        self.name = name
        self.fam = fam
        self.id = uuid.uuid4()


def __str__(self):
    return f"{self.id}"