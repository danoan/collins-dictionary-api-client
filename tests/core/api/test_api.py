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
