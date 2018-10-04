import sys
from .commands import *


def main():
    args = sys.argv[1:]

    if not args:
        wh_help()

    elif args[0] == 'graph':
        graph(args)

    elif args[0] == 'help':
        wh_help()

    else:
        wh_help(args)

if __name__ == '__main__':
    main()
