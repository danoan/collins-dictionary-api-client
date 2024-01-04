#! /usr/bin/env python3

import argparse

from collins_dictionary_api_client import api_client


def main():
    parser = argparse.ArgumentParser(description="CLI to the Collins API.")

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
        type=api_client.Language,
        choices=list(api_client.Language),
        default=api_client.Language.English,
        help="Language of the dictionary.",
    )

    subparsers = parser.add_subparsers()

    parser_get_best_matching = subparsers.add_parser("get-best-matching")
    parser_get_best_matching.add_argument("word")
    parser_get_best_matching.set_defaults(func=api_client.get_best_matching)

    parser_get_entry = subparsers.add_parser("get-entry")
    parser_get_entry.add_argument("entry_id")
    parser_get_entry.set_defaults(func=api_client.get_entry)

    args = parser.parse_args()

    if "func" in args:
        http_response = args.func(**vars(args))
        print(http_response.text)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
