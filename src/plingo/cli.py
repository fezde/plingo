from interpreter import Plingo
from sys import argv
import logging
import argparse
import sys
import progressbar


def main():
    log_level = logging.WARN
    show_progressbar = True

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
        show_progressbar = True
    elif args.loginfo:
        log_level = logging.INFO
        show_progressbar = True
    elif args.logerror:
        log_level = logging.ERROR
        show_progressbar = False
    else:
        log_level = logging.WARN
        show_progressbar = True

    progressbar.streams.wrap_stderr()
    logging.basicConfig(level=log_level)
    lingo = Plingo(args.file)
    lingo.execute(show_progressbar=show_progressbar)


if __name__ == "__main__":
    main()
