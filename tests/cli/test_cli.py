from danoan.dictionaries.collins.cli import cli


def test_get_parser():
    parser = cli.get_parser()
    assert parser is not None
