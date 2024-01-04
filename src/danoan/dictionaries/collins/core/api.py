from danoan.dictionaries.collins.core import model

import requests


def get_best_matching(
    entrypoint: str, secret_key: str, language: model.Language, word: str, **kargs
) -> requests.Response:
    """
    Get the first result found for the searched word.
    """
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
    entrypoint: str, secret_key: str, language: model.Language, entry_id: str, **kargs
) -> requests.Response:
    """
    Return metadata corresponding to an entry id.
    """
    headers = {
        "Host": "localhost",
        "Accept": "application/xml",
        "accessKey": secret_key,
    }
    return requests.get(
        f"{entrypoint}/dictionaries/{language}/entries/{entry_id}?format=html",
        headers=headers,
    )
