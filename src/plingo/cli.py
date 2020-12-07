from interpreter import Plingo
from sys import argv
import logging
import argparse
import sys


def main():
    log_level = logging.WARN

    parser = argparse.ArgumentParser(description='Execute a Plingo program')
    parser.add_argument(
        'file',
        metavar='FILE',
        help='the image file containing the Plingo code')

    parser.add_argument(
        '-v',
        dest='loginfo',
        action='store_true',
        help='verbose output')

    parser.add_argument(
        '-vv',
        dest='logdebug',
        action='store_true',
        help='very verbose output')

    parser.add_argument(
        '-q',
        dest='logerror',
        action='store_true',
        help='no output at all')

    args = parser.parse_args()

    if not args.file:
        parser.print_help()
        sys.exit(1)

    if args.logdebug:
        log_level = logging.DEBUG
    elif args.loginfo:
        log_level = logging.INFO
    elif args.logerror:
        log_level = logging.ERROR
    else:
        log_level = logging.WARN

    logging.basicConfig(level=log_level)
    lingo = Plingo(args.file)
    lingo.execute()


if __name__ == "__main__":
    main()
