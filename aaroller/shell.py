import cmd
from inspect import getdoc

from colorama import Fore

from aaroller.dice import roll, record, stats, stat_reset, save, retrieve


class DiceShell(cmd.Cmd):
    intro = """Welcome to simple dice. Type help or ? to list commands.\n"""
    prompt = Fore.BLUE + '>> ' + Fore.RESET

    def do_x_roll(self, arg):
        """Roll a number of dice with a hit level. Example: ROLL 10 3"""
        self._do_roll(arg, 'Axis')

    def do_a_roll(self, arg):
        """Roll a number of dice with a hit level. Example: ROLL 10 3"""
        self._do_roll(arg, 'Allies')

    def _do_roll(self, arg, player):
        """Roll a number of dice with a hit level. Example: ROLL 10 3"""
        try:
            args = arg.split()
            assert len(args) == 2
            params = int(args[0]), int(args[1])
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
        """Gives summary of all rolls so far"""
        if arg == "reset":
            stat_reset()
        else:
            print(Fore.BLUE + "          Expected   Hits  Rolls    Luck" + Fore.RESET)
            stat_lines = '\n'.join(line for line in stats())
            print(stat_lines)

    def do_save(self, arg):
        """Saves current stats with name given"""
        assert len(arg) > 0 and ' ' not in arg
        save(arg)

    def do_open(self, arg):
        """Retrieves named stats"""
        assert len(arg) > 0 and ' ' not in arg
        retrieve(arg)

    def do_exit(self, arg):
        """Say goodbye and exit"""
        print('Goodbye.')
        return True

    def do_EOF(self, arg):
        """Say goodbye and exit"""
        print('Goodbye.')
        return True


def main():
    DiceShell().cmdloop()
