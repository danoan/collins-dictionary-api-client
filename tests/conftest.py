def pytest_addoption(parser):
    parser.addoption("--secret-key", action="store")
    parser.addoption("--entrypoint", action="store")
