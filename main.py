import cmd
from inspect import getdoc

from dice import roll, record, stats


class DiceShell(cmd.Cmd):
    intro = """Welcome to simple dice. Type help or ? to list commands.\n"""
    prompt = '>> '

    def do_x_roll(self, arg):
        """Roll a number of dice with a hit level. Example: ROLL 10 3"""
        self._do_roll(arg, 'x')

    def do_a_roll(self, arg):
        """Roll a number of dice with a hit level. Example: ROLL 10 3"""
        self._do_roll(arg, 'a')

    def _do_roll(self, arg, player):
        """Roll a number of dice with a hit level. Example: ROLL 10 3"""
        try:
            params = parse(arg)
            assert len(params) == 2
            results = roll(*params)
            record(results.results, player)
            print(results)
        except ValueError:
            print("Unable to parse integer arguments")
            print(getdoc(self._do_roll))
        except AssertionError:
            print("Incorrect number of arguments")
            print(getdoc(self._do_roll))

    def do_stats(self, arg):
        stat_lines = '\n'.join(line for line in stats())
        print(stat_lines)

    def do_exit(self, arg):
        """Say goodbye and exit"""
        print('Goodbye.')
        exit()


def parse(arg):
    """Convert a series of zero or more numbers to an argument tuple"""
    args = arg.split()
    return int(args[0]), int(args[1])

if __name__ == '__main__':
    DiceShell().cmdloop()
