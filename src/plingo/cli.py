import argparse
import logging
import sys

import progressbar

from . import __version__
from . import Plingo


def main():
    log_level = logging.WARN
    show_progressbar = True

    parser = argparse.ArgumentParser(description="Execute a Plingo program")
    parser.add_argument(
        "file", metavar="FILE", help="the image file containing the Plingo code"
    )

    parser.add_argument(
        "-v", dest="loginfo", action="store_true", help="verbose output"
    )

    parser.add_argument(
        "-vv", dest="logdebug", action="store_true", help="very verbose output"
    )

    parser.add_argument(
        "-i",
        "--iterations",
        type=int,
        dest="iterations",
        help="The number of iterations",
    )

    parser.add_argument(
        "-q", dest="logerror", action="store_true", help="no output at all"
    )

    parser.add_argument(
        "-version",
        "--version",
        action="version",
        version=f"plingo version {__version__}",
    )

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
    iterations = 1
    if args.iterations:
        iterations = args.iterations
    lingo.execute(show_progressbar=show_progressbar, iterations=iterations)


if __name__ == "__main__":
    main()
