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

    def __repr__(self):
        return '<num: %d, hit_level: %d, hit: %s>' % (self.num, self.hit_level, self.hit)


class Results(object):

    def __init__(self, results):
        self.results = results
        self.count = [result.hit for result in results].count(True)

    def __str__(self):
        roll_str = "Rolls: %s" % ''.join([str(r) for r in self.results])
        return "Hits: %s\n%s" % (self.count, roll_str if len(self.results) < 25 else '')


class Stat(object):

    def __init__(self, player):
        self.rolls = []
        self.player = player

    def update(self, results):
        self.rolls.extend(results)

    def find_exp_act(self):
        expected = sum([r.hit_level for r in self.rolls])/6
        actual = [r.hit for r in self.rolls].count(True)
        return expected, actual, len(self.rolls)

    def stat_line(self):
        exp, act, num = self.find_exp_act()
        return '%6s>> Expected Hits: %6.1f, Hits: %4d, Rolls: %4d, Luck %%: %5.1f%%' %\
               (self.player, exp, act, num, (act - exp)*100/num)


all_results = {}


def record(results, player):
    global all_results
    if player not in all_results:
        all_results[player] = Stat(player)
    all_results[player].update(results)


def stats():
    global all_results
    return [all_results[k].stat_line() for k in all_results]


def stat_reset():
    global all_results
    all_results = {}
