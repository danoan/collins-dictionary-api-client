"""
Model classes for the collins.core package.
"""
from enum import Enum


class Language(Enum):
    English = "english"

    def __str__(self):
        return self.value


class Format(Enum):
    JSON = "json"
    XML = "xml"

    def __str__(self):
        return self.value
