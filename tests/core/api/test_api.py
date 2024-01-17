"""
The goal of these tests is to make sure that the API endpoints are working.
We are not particularly interested in the content of the response, but
actually in the success of the request.
"""

from danoan.dictionaries.collins.core import api, model

from bs4 import BeautifulSoup
import os
import json
from pathlib import Path
import pytest
import warnings
from typing import Any

SCRIPT_FOLDER = Path(os.path.abspath(__file__)).parent


class DataAdapter:
    def __init__(self, data: Any, format: model.Format):
        self.format = format
        if format == model.Format.JSON:
            self.data = json.loads(data)
        elif format == model.Format.XML:
            self.data = BeautifulSoup(data, "xml")

    def get_field(self, field_name: str):
        if self.format == model.Format.JSON:
            return self.data[field_name]
        elif self.format == model.Format.XML:
            return self.data.find(field_name)


@pytest.fixture(scope="session")
def secret_key(pytestconfig):
    v = pytestconfig.getoption("secret_key")
    if v is None:
        warnings.warn("The secret_key is not specified. Test won't be executed.")
    return pytestconfig.getoption("secret_key", skip=True)


@pytest.fixture(scope="session")
def entrypoint(pytestconfig):
    v = pytestconfig.getoption("entrypoint")
    if v is None:
        warnings.warn("The entrypoint not specified. Test won't be executed.")
    return pytestconfig.getoption("entrypoint", skip=True)


@pytest.mark.parametrize(
    "language, word, format",
    [
        (model.Language.English, "legitim", model.Format.XML),
        (model.Language.English, "legitim", model.Format.JSON),
    ],
)
def test_search(language, word, format, entrypoint, secret_key):
    response = api.search(entrypoint, secret_key, language, word, format=format)
    assert response.status_code == 200

    adapter = DataAdapter(response.text, format)

    print(adapter.get_field("dictionaryCode"))
    print(adapter.get_field("results"))

    assert len(str(adapter.get_field("dictionaryCode")).strip()) > 0
    assert len(str(adapter.get_field("results")).strip()) > 0


@pytest.mark.parametrize(
    "language, word, format",
    [
        (model.Language.English, "legitim", model.Format.XML),
        (model.Language.English, "legitim", model.Format.JSON),
    ],
)
def test_did_you_mean(language, word, format, entrypoint, secret_key):
    response = api.did_you_mean(entrypoint, secret_key, language, word, format=format)
    assert response.status_code == 200

    adapter = DataAdapter(response.text, format)

    print(adapter.get_field("dictionaryCode"))
    print(adapter.get_field("suggestions"))

    assert len(str(adapter.get_field("dictionaryCode")).strip()) > 0
    assert len(str(adapter.get_field("suggestions")).strip()) > 0


@pytest.mark.parametrize(
    "language, word, format",
    [
        (model.Language.English, "legitim", model.Format.XML),
        (model.Language.English, "legitim", model.Format.JSON),
    ],
)
def test_best_matching(language, word, format, entrypoint, secret_key):
    response = api.get_best_matching(
        entrypoint, secret_key, language, word, format=format
    )
    assert response.status_code == 200

    adapter = DataAdapter(response.text, format)

    print(adapter.get_field("dictionaryCode"))
    print(adapter.get_field("entryLabel"))

    assert len(str(adapter.get_field("dictionaryCode")).strip()) > 0
    assert len(str(adapter.get_field("entryLabel")).strip()) > 0


@pytest.mark.parametrize(
    "language, entry_id, format",
    [
        (model.Language.English, "legitim_1", model.Format.XML),
        (model.Language.English, "legitim_1", model.Format.JSON),
    ],
)
def test_get_entry(language, entry_id, format, entrypoint, secret_key):
    response = api.get_entry(entrypoint, secret_key, language, entry_id, format=format)
    assert response.status_code == 200

    adapter = DataAdapter(response.text, format)

    print(adapter.get_field("dictionaryCode"))
    print(adapter.get_field("entryLabel"))

    assert len(str(adapter.get_field("dictionaryCode")).strip()) > 0
    assert len(str(adapter.get_field("entryLabel")).strip()) > 0


@pytest.mark.parametrize(
    "language, entry_id, format",
    [
        (model.Language.English, "happy_1", model.Format.XML),
        (model.Language.English, "happy_1", model.Format.JSON),
    ],
)
def test_get_pronunciations(language, entry_id, format, entrypoint, secret_key):
    response = api.get_pronunciations(
        entrypoint, secret_key, language, entry_id, format=format
    )
    assert response.status_code == 200

    if format == model.Format.JSON:
        data = json.loads(response.text)[0]
        data = json.dumps(data)
    else:
        data = response.text

    adapter = DataAdapter(data, format)

    print(adapter.get_field("dictionaryCode"))
    print(adapter.get_field("pronunciationUrl"))

    assert len(str(adapter.get_field("dictionaryCode")).strip()) > 0
    assert len(str(adapter.get_field("pronunciationUrl")).strip()) > 0


@pytest.mark.parametrize(
    "language, entry_id, format",
    [
        (model.Language.English, "happy_1", model.Format.XML),
        (model.Language.English, "happy_1", model.Format.JSON),
    ],
)
def test_get_nearby_entries(language, entry_id, format, entrypoint, secret_key):
    response = api.get_nearby_entries(
        entrypoint, secret_key, language, entry_id, format=format
    )
    assert response.status_code == 200

    adapter = DataAdapter(response.text, format)

    print(adapter.get_field("dictionaryCode"))
    print(adapter.get_field("nearbyFollowingEntries"))

    assert len(str(adapter.get_field("dictionaryCode")).strip()) > 0
    assert len(str(adapter.get_field("nearbyFollowingEntries")).strip()) > 0
