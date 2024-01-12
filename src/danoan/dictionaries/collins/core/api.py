from danoan.dictionaries.collins.core import model

import requests
from typing import Optional


def get_search(
    entrypoint: str,
    secret_key: str,
    language: model.Language,
    word: str,
    page_size: int = 10,
    page_index: int = 1,
    **kargs,
) -> requests.Response:
    """
    Get a list of results corresponding to the search term.
    """
    headers = {
        "Host": "localhost",
        "Accept": "application/xml",
        "accessKey": secret_key,
    }
    return requests.get(
        f"{entrypoint}/dictionaries/{language.value}/search/?q={word}&pagesize={page_size}&pageindex={page_index}",
        headers=headers,
    )


def get_did_you_mean(
    entrypoint: str,
    secret_key: str,
    language: model.Language,
    word: str,
    entry_number: int = 10,
    **kargs,
) -> requests.Response:
    """
    Get a list of suggestions corresponding to the input word.
    """
    headers = {
        "Host": "localhost",
        "Accept": "application/xml",
        "accessKey": secret_key,
    }
    return requests.get(
        f"{entrypoint}/dictionaries/{language.value}/search/didyoumean/?q={word}&entrynumber={entry_number}",
        headers=headers,
    )


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


def get_pronunciation(
    entrypoint: str,
    secret_key: str,
    language: model.Language,
    entry_id: str,
    lang: Optional[model.Language] = None,
    **kargs,
) -> requests.Response:
    """
    Get a list of pronunciations.

    Each pronunciation entry contains a URL to a mp3 file.
    """
    headers = {
        "Host": "localhost",
        "Accept": "application/xml",
        "accessKey": secret_key,
    }

    args = [""]
    if lang:
        args.append("?")
        args.append("lang=")
        args.append(lang)

    return requests.get(
        f"{entrypoint}/dictionaries/{language}/entries/{entry_id}/pronunciations{''.join(args)}",
        headers=headers,
    )


def get_nearby_entries(
    entrypoint: str,
    secret_key: str,
    language: model.Language,
    entry_id: str,
    entry_number: int = 10,
    **kargs,
) -> requests.Response:
    """
    Get a list of entries similar (synonymous or related) to the input word.
    """
    headers = {
        "Host": "localhost",
        "Accept": "application/xml",
        "accessKey": secret_key,
    }

    return requests.get(
        f"{entrypoint}/dictionaries/{language}/entries/{entry_id}/nearbyentries?entrynumber={entry_number}",
        headers=headers,
    )
