from danoan.dictionaries.collins.core import api, model

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

    expected_response = SCRIPT_FOLDER / "expected" / "get_best_matching.xml"
    # with open(expected_response, "w") as f:
    #     f.write(response.text)

    with open(expected_response, "r") as f:
        for expected_line, output_line in zip(
            f.readlines(), response.text.splitlines()
        ):
            assert expected_line.strip() == output_line.strip()


@pytest.mark.parametrize(
    "language, entry_id",
    [(model.Language.English, "legitim_1")],
)
def test_get_entry(language, entry_id, entrypoint, secret_key):
    response = api.get_entry(entrypoint, secret_key, language, entry_id)

    expected_response = SCRIPT_FOLDER / "expected" / "get_entry.xml"
    # with open(expected_response, "w") as f:
    #     f.write(response.text)

    with open(expected_response, "r") as f:
        for expected_line, output_line in zip(
            f.readlines(), response.text.splitlines()
        ):
            assert expected_line.strip() == output_line.strip()
