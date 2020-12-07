from plingo import Plingo
from sys import argv

if __name__ == "__main__":
    lingo = Plingo(argv[1])
    lingo.execute()
