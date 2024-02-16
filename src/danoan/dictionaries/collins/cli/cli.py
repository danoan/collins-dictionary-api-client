#! /usr/bin/env python3

import argparse

from danoan.dictionaries.collins.core import api
from danoan.dictionaries.collins.core import model


def get_parser():
    parser = argparse.ArgumentParser(
        description="CLI to the Collins API.",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--secret-key", required=True, help="Your secret key to make API calls."
    )
    parser.add_argument(
        "--entrypoint",
        default="https://api.collinsdictionary.com/api/v1",
        help="Link to send API requests.",
    )
    parser.add_argument(
        "--language",
        type=model.Language,
        choices=list(model.Language),
        default=model.Language.English,
        help="Language of the dictionary.",
    )
    parser.add_argument(
        "--format",
        default="json",
        choices=[str(x) for x in model.Format],
        help="Format of response.",
    )

    subparsers = parser.add_subparsers()

    def get_description(x):
        return x.__doc__

    def get_help(x):
        return x.__doc__.split(".")[0]

    parser_search = subparsers.add_parser(
        "search",
        description=get_description(api.search),
        help=get_help(api.search),
    )
    parser_search.add_argument("word")
    parser_search.set_defaults(func=api.search)

    parser_did_you_mean = subparsers.add_parser(
        "did-you-mean",
        description=get_description(api.did_you_mean),
        help=get_help(api.did_you_mean),
    )
    parser_did_you_mean.add_argument("word")
    parser_did_you_mean.set_defaults(func=api.did_you_mean)

    parser_get_best_matching = subparsers.add_parser(
        "get-best-matching",
        description=get_description(api.get_best_matching),
        help=get_help(api.get_best_matching),
    )
    parser_get_best_matching.add_argument("word")
    parser_get_best_matching.set_defaults(func=api.get_best_matching)

    parser_get_entry = subparsers.add_parser(
        "get-entry",
        description=get_description(api.get_entry),
        help=get_help(api.get_entry),
    )
    parser_get_entry.add_argument("entry_id")
    parser_get_entry.set_defaults(func=api.get_entry)

    parser_get_pronunciations = subparsers.add_parser(
        "get-pronunciations",
        description=get_description(api.get_pronunciations),
        help=get_help(api.get_pronunciations),
    )
    parser_get_pronunciations.add_argument("entry_id")
    parser_get_pronunciations.set_defaults(func=api.get_pronunciations)

    parser_get_nearby_entries = subparsers.add_parser(
        "get-nearby-entries",
        description=get_description(api.get_nearby_entries),
        help=get_help(api.get_nearby_entries),
    )
    parser_get_nearby_entries.add_argument("entry_id")
    parser_get_nearby_entries.set_defaults(func=api.get_nearby_entries)

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    if "func" in args:
        http_response = args.func(**vars(args))
        print(http_response.text)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
