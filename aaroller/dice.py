from random import randint
import json

from colorama import Fore


def roll(number, hit_level):
    rolls = [Roll(hit_level) for _ in range(number)]
    return Results(rolls)


class Roll(object):

    def __init__(self, hit_level):
        self.num = randint(1,6)
        self.hit_level = hit_level
        self.hit = self.num <= self.hit_level

    def __str__(self):
        return '%s[%s]%s' % (Fore.RED, self.num, Fore.RESET) if self.hit else ' %s ' % self.num

    def __repr__(self):
        return '<num: %d, hit_level: %d, hit: %s>' % (self.num, self.hit_level, self.hit)


class Results(object):

    def __init__(self, results):
        self.results = results
        self.count = [result.hit for result in results].count(True)

    def __str__(self):
        roll_str = "Rolls: %s" % ''.join([str(r) for r in self.results])
        return "%sHits: %s%s\n%s" % (Fore.GREEN, self.count, Fore.RESET, roll_str if len(self.results) < 25 else '')


class Stat(object):

    def __init__(self, player):
        self.player = player
        self.rolls, self.exp, self.act = 0, 0, 0

    def update(self, results):
        self.rolls += len(results)
        self.exp += sum([r.hit_level for r in results])/6
        self.act += [r.hit for r in results].count(True)

    def stat_line(self):
        luck = (self.act - self.exp)*100/self.rolls
        if luck > 4:
            luck_color = Fore.GREEN
        elif luck < -4:
            luck_color = Fore.RED
        else:
            luck_color = Fore.WHITE
        return '%s%6s>>%s %9.1f%7d%7d%s%7.1f%%%s' %\
               (Fore.BLUE, self.player, Fore.RESET,
                self.exp, self.act, self.rolls,
                luck_color, luck, Fore.RESET)


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


def save(filename):
    global all_results
    results_dict = {k: {'player': all_results[k].player,
                        'rolls': all_results[k].rolls,
                        'exp': all_results[k].exp,
                        'act': all_results[k].act} for k in all_results}
    with open(filename + '.json', 'w') as save_file:
        save_file.write(json.dumps(results_dict))


def retrieve(filename):
    global all_results
    with open(filename + '.json', 'r') as retrieve_file:
        stuff = json.loads(retrieve_file.read())
    for k in stuff:
        s = Stat(stuff[k]['player'])
        s.act = stuff[k]['act']
        s.exp = stuff[k]['exp']
        s.rolls = stuff[k]['rolls']
        all_results[k] = s
