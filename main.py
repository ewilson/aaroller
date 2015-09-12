import cmd
from inspect import getdoc

from dice import roll


class DiceShell(cmd.Cmd):
    intro = """Welcome to simple dice. Type help or ? to list commands.\n"""
    prompt = '>> '

    def do_roll(self, arg):
        """Roll a number of dice with a hit level. Example: ROLL 10 3"""
        try:
            params = parse(arg)
            assert len(params) == 2
            print(roll(*params))
        except ValueError:
            print("Unable to parse integer arguments")
            print(getdoc(self.do_roll))
        except AssertionError:
            print("Incorrect number of arguments")
            print(getdoc(self.do_roll))

    def do_exit(self, arg):
        """Say goodbye and exit"""
        print('Goodbye.')
        exit()


def parse(arg):
    """Convert a series of zero or more numbers to an argument tuple"""
    args = arg.split()
    return [int(s) for s in args]

if __name__ == '__main__':
    DiceShell().cmdloop()