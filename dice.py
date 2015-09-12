from random import randint


def roll(number, hit_level):
    rolls = [Roll(hit_level) for _ in range(number)]
    return Results(rolls)


class Roll(object):

    def __init__(self, hit_level):
        self.num = randint(1,6)
        self.hit_level = hit_level
        self.hit = self.num <= self.hit_level

    def __str__(self):
        return '[%s]' % self.num if self.hit else ' %s ' % self.num


class Results(object):

    def __init__(self, results):
        self.results = results
        self.count = [result.hit for result in results].count(True)

    def __str__(self):
        roll_str = "Rolls: %s" % ''.join([str(r) for r in self.results])
        return "Hits: %s\n%s" % (self.count, roll_str if len(self.results) < 25 else '')


def get_input():
    while True:
        input_str = input('>> ').strip()
        if input_str[0].lower() == 'q':
            exit()
        try:
            return [int(s) for s in input_str.split(' ')]
        except ValueError:
            print('>%s< is invalid input.' % input_str)

if __name__ == '__main__':
    while True:
        dice, level = get_input()
        print(roll(dice, level))
