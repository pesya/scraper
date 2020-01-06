import argparse

from scraper.commands import fetch, crawl


def execute():
    parser = argparse.ArgumentParser(prog='scraper')
    subparsers = parser.add_subparsers()

    parser_fetch = subparsers.add_parser('fetch')
    parser_fetch.add_argument('url', type=str, help='url for fetching')
    parser_fetch.set_defaults(func=fetch.execute)

    parser_crawl = subparsers.add_parser('crawl')
    parser_crawl.add_argument(
        '-f',
        '--format',
        default='csv',
        choices=['csv', 'jl'],
        help='format of output file',
    )
    parser_crawl.set_defaults(func=crawl.execute)

    args = parser.parse_args()
    args.func(args)