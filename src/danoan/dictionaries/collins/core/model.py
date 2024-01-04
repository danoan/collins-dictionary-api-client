from enum import Enum


class Language(Enum):
    English = "english"

    def __str__(self):
        return self.value
