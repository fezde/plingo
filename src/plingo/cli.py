from interpreter import Plingo
from sys import argv


def main():
    lingo = Plingo(argv[1])
    lingo.execute()


if __name__ == "__main__":
    main()
