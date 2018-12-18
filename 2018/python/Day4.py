import datetime
import collections
import itertools

class Entry:

    def __init__(self, date, action):
        self.date = date
        self.action = action

    def __repr__(self):
        return " ".join((str(self.date), self.action))

    @staticmethod
    def parse_line(line):
        date, action = line.split(']')
        date, hour = date[1:].split()
        year, month, day = date.split('-')
        hour, minute = hour.split(':')
        date = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
        return Entry(date, action)

class Guard:

    def __init__(self, id):
        self.sleep_times = collections.defaultdict(list)
        self.id = id
        self.total_sleep = 0

    def add_sleep(self, init, end):
        day = init.strftime('%m%d')
        period = init.minute, end.minute
        self.total_sleep += (end.minute - init.minute)
        self.sleep_times[day].append(period)
    
    def __repr__(self):
        return " ".join((self.id, str(self.total_sleep)))

    def get_best_minute(self):
        counter = collections.Counter()
        for st in self.sleep_times.values():
            for t in st:
                counter.update(range(t[0],t[1]))
        try:                
            return counter.most_common(1)[0]
        except:
            return 0,0



def readIn(fName="d:/Sandbox/advent/2018/input4"):
    l = []
    with open(fName) as f:
        l = (i.strip() for i in f.readlines())
    return l


def puzzle1(l):
    ordered = sorted(map(Entry.parse_line, l), key=lambda x:x.date)
    guards = {}
    current = None
    init = None
    for e in ordered:
        split = e.action.split()
        if len(split) > 2:
            id = split[1][1:]
            current = guards.setdefault(id, Guard(id))
        elif split[0] == "falls":
            init = e.date
        elif split[0] == "wakes":
            current.add_sleep(init, e.date)

    target_guard = max(guards.values(), key=lambda x:x.total_sleep)
    print(target_guard)
    best = target_guard.get_best_minute()
    print(int(best[0]) * int(target_guard.id))

def puzzle2(l):
    ordered = sorted(map(Entry.parse_line, l), key=lambda x:x.date)
    guards = {}
    current = None
    init = None
    for e in ordered:
        split = e.action.split()
        if len(split) > 2:
            id = split[1][1:]
            current = guards.setdefault(id, Guard(id))
        elif split[0] == "falls":
            init = e.date
        elif split[0] == "wakes":
            current.add_sleep(init, e.date)
    
    best_minutes = []
    for g in guards.values():
        m, t = g.get_best_minute()
        best_minutes.append((g.id, m ,t))
    target = max(best_minutes, key=lambda x : x[2])
    print(target)
    print(int(target[0]) * int(target[1]))


if __name__ == '__main__':
    # puzzle1(readIn("d:/Sandbox/advent/2018/input4Test"))
    puzzle1(readIn())
    # puzzle2(list(readIn("d:/Sandbox/advent/2018/input4Test")))
    puzzle2(list(readIn()))
