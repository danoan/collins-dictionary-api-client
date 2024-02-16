"""
Client to the Collins dictionary API.
"""
from danoan.dictionaries.collins.core import model

import requests
from typing import Optional


def search(
    entrypoint: str,
    secret_key: str,
    language: model.Language,
    word: str,
    page_size: int = 10,
    page_index: int = 1,
    format: model.Format = model.Format.JSON,
    **kargs,
) -> requests.Response:
    """
    Get a list of entry ids corresponding to the search term.
    """
    headers = {
        "Host": "localhost",
        "Accept": f"application/{format}",
        "accessKey": secret_key,
    }
    return requests.get(
        f"{entrypoint}/dictionaries/{language.value}/search/?q={word}&pagesize={page_size}&pageindex={page_index}",
        headers=headers,
    )


def did_you_mean(
    entrypoint: str,
    secret_key: str,
    language: model.Language,
    word: str,
    entry_number: int = 10,
    format: model.Format = model.Format.JSON,
    **kargs,
) -> requests.Response:
    """
    Get a list of suggestions corresponding to the input word.

    The suggested words are close to the input word in a lexicographic sense.
    For example, share a good portion of the prefix or the suffix.
    """
    headers = {
        "Host": "localhost",
        "Accept": f"application/{format}",
        "accessKey": secret_key,
    }
    return requests.get(
        f"{entrypoint}/dictionaries/{language.value}/search/didyoumean/?q={word}&entrynumber={entry_number}",
        headers=headers,
    )


def get_best_matching(
    entrypoint: str,
    secret_key: str,
    language: model.Language,
    word: str,
    format: model.Format = model.Format.JSON,
    **kargs,
) -> requests.Response:
    """
    Get the metadata of the first entry found for the searched word.
    """
    headers = {
        "Host": "localhost",
        "Accept": f"application/{format}",
        "accessKey": secret_key,
    }
    return requests.get(
        f"{entrypoint}/dictionaries/{language.value}/search/first/?q={word}",
        headers=headers,
    )


def get_entry(
    entrypoint: str,
    secret_key: str,
    language: model.Language,
    entry_id: str,
    format: model.Format = model.Format.JSON,
    **kargs,
) -> requests.Response:
    """
    Get the metadata corresponding to an entry id.
    """
    headers = {
        "Host": "localhost",
        "Accept": f"application/{format}",
        "accessKey": secret_key,
    }
    return requests.get(
        f"{entrypoint}/dictionaries/{language}/entries/{entry_id}?format=html",
        headers=headers,
    )


def get_pronunciations(
    entrypoint: str,
    secret_key: str,
    language: model.Language,
    entry_id: str,
    lang: Optional[model.Language] = None,
    format: model.Format = model.Format.JSON,
    **kargs,
) -> requests.Response:
    """
    Get a list of pronunciations.

    Each pronunciation entry contains a URL to a mp3 file.
    """
    headers = {
        "Host": "localhost",
        "Accept": f"application/{format}",
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
    format: model.Format = model.Format.JSON,
    **kargs,
) -> requests.Response:
    """
    Get a list of entries related to the input word.

    The returned words or expressions are in the same semantic scope of the input word.
    """
    headers = {
        "Host": "localhost",
        "Accept": f"application/{format}",
        "accessKey": secret_key,
    }

    return requests.get(
        f"{entrypoint}/dictionaries/{language}/entries/{entry_id}/nearbyentries?entrynumber={entry_number}",
        headers=headers,
    )
