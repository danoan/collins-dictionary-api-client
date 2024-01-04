from enum import Enum

import requests


class Language(Enum):
    English = "english"

    def __str__(self):
        return self.value


# ---------------- API Request ------------------
def get_best_matching(
    entrypoint: str, secret_key: str, language: Language, word: str, **kargs
) -> requests.Response:
    headers = {
        "Host": "localhost",
        "Accept": "application/xml",
        "accessKey": secret_key,
    }
    return requests.get(
        f"{entrypoint}/dictionaries/{language.value}/search/first/?q={word}&format=xml",
        headers=headers,
    )


def get_entry(
    entrypoint: str, secret_key: str, language: Language, entry_id: str, **kargs
) -> requests.Response:
    headers = {
        "Host": "localhost",
        "Accept": "application/xml",
        "accessKey": secret_key,
    }
    return requests.get(
        f"{entrypoint}/dictionaries/{language}/entries/{entry_id}?format=html",
        headers=headers,
    )
