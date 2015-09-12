from random import randint
from collections import Counter

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


all_results = Counter()


def record(results):
    global all_results
    all_results.update([r.num for r in results])


def stats():
    global all_results
    return all_results
