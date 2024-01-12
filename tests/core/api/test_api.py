"""
The goal of these tests is to make sure that the API endpoints are working.
We are not particularly interested in the content of the response, but
actually in the success of the request.
"""

from danoan.dictionaries.collins.core import api, model

from bs4 import BeautifulSoup
import os
from pathlib import Path
import pytest
import warnings

SCRIPT_FOLDER = Path(os.path.abspath(__file__)).parent


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
    "language, word",
    [(model.Language.English, "legitim")],
)
def test_get_search(language, word, entrypoint, secret_key):
    response = api.get_search(entrypoint, secret_key, language, word)
    assert response.status_code == 200

    xml_response = BeautifulSoup(response.text, "xml")

    print(xml_response.find("dictionaryCode"))
    print(xml_response.find("entryLabel"))

    assert (
        str(xml_response.find("dictionaryCode"))
        == "<dictionaryCode>english</dictionaryCode>"
    )
    assert str(xml_response.find("entryLabel")) == "<entryLabel>legitim</entryLabel>"


@pytest.mark.parametrize(
    "language, word",
    [(model.Language.English, "legitim")],
)
def test_get_did_you_mean(language, word, entrypoint, secret_key):
    response = api.get_did_you_mean(entrypoint, secret_key, language, word)
    assert response.status_code == 200

    xml_response = BeautifulSoup(response.text, "xml")

    print(xml_response.find("dictionaryCode"))
    print(xml_response.find("suggestions"))
    print(xml_response.find("suggestion"))

    assert (
        str(xml_response.find("dictionaryCode"))
        == "<dictionaryCode>english</dictionaryCode>"
    )
    assert len(str(xml_response.find("suggestions"))) > 0
    assert len(str(xml_response.find("suggestion"))) > 0


@pytest.mark.parametrize(
    "language, word",
    [(model.Language.English, "legitim")],
)
def test_best_matching(language, word, entrypoint, secret_key):
    response = api.get_best_matching(entrypoint, secret_key, language, word)
    assert response.status_code == 200

    xml_response = BeautifulSoup(response.text, "xml")

    print(xml_response.find("dictionaryCode"))
    print(xml_response.find("entryLabel"))

    assert (
        str(xml_response.find("dictionaryCode"))
        == "<dictionaryCode>english</dictionaryCode>"
    )
    assert str(xml_response.find("entryLabel")) == "<entryLabel>legitim</entryLabel>"


@pytest.mark.parametrize(
    "language, entry_id",
    [(model.Language.English, "legitim_1")],
)
def test_get_entry(language, entry_id, entrypoint, secret_key):
    response = api.get_entry(entrypoint, secret_key, language, entry_id)
    assert response.status_code == 200

    xml_response = BeautifulSoup(response.text, "xml")

    print(xml_response.find("dictionaryCode"))
    print(xml_response.find("entryLabel"))

    assert (
        str(xml_response.find("dictionaryCode"))
        == "<dictionaryCode>english</dictionaryCode>"
    )
    assert str(xml_response.find("entryLabel")) == "<entryLabel>legitim</entryLabel>"


@pytest.mark.parametrize(
    "language, entry_id",
    [(model.Language.English, "happy_1")],
)
def test_get_pronunciation(language, entry_id, entrypoint, secret_key):
    response = api.get_pronunciation(entrypoint, secret_key, language, entry_id)
    assert response.status_code == 200

    xml_response = BeautifulSoup(response.text, "xml")

    print(xml_response.find("dictionaryCode"))
    print(xml_response.find("pronunciations"))
    print(xml_response.find("pronunciation"))

    assert (
        str(xml_response.find("dictionaryCode"))
        == "<dictionaryCode>english</dictionaryCode>"
    )
    assert len(str(xml_response.find("pronunciations"))) > 0
    assert len(str(xml_response.find("pronunciation"))) > 0


@pytest.mark.parametrize(
    "language, entry_id",
    [(model.Language.English, "happy_1")],
)
def test_get_nearby_entries(language, entry_id, entrypoint, secret_key):
    response = api.get_nearby_entries(entrypoint, secret_key, language, entry_id)
    assert response.status_code == 200

    xml_response = BeautifulSoup(response.text, "xml")

    print(xml_response.find("dictionaryCode"))
    print(xml_response.find("nearbyFollowingEntries"))
    print(xml_response.find("nearbyEntry"))

    assert (
        str(xml_response.find("dictionaryCode"))
        == "<dictionaryCode>english</dictionaryCode>"
    )
    assert len(str(xml_response.find("nearbyFollowingEntries"))) > 0
    assert len(str(xml_response.find("nearbyEntry"))) > 0
