from fletch_tools.good_input import get_input

def graph(args):
    name = get_input('What is your name?')
    print('Hello {}.'.format(name))

def wh_help(args=''):
    if args:
        print("\n{}'{}' didn't trigger any commands!"
            .format('  ', ' '.join(args)))
    else:
        print(
            '\n  Text Grapher'
            )
    print(
        """
  Commands:

  wh help              - Show help and exit.
  wh graph             - Fire up the graphing process.
        """
    )
