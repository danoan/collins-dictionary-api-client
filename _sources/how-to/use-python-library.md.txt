# How to use the python library

The Collins Dictionary API Client is packed with a python library that can be
imported in your projects.

## Installation

```bash
pip install collins-dictionary-api
```

To test the installation

```bash
$ python
>>> from danoan.dictionaries.collins.core import api as collins_api

```

## Calling an API method

The list of available methods can be consulted [here](../getting-started.md#methods-available)
```python
>>> from danoan.dictionaries.collins.core import api as collins_api

entrypoint=""
secret_key="MY_SECRET_KEY"

collins_api.search(
    entrypoint,
    secret_key,
    collins_api.model.Language.English,
    "legitim",
    format = collins_apo.model.Format.JSON
)
```

```{admonition} Output formats
Output is available in JSON and XML format.
```
