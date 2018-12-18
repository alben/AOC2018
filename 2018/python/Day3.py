import collections
import itertools

def readIn(fName="d:/Sandbox/advent/2018/input3"):
    l = []

    with open(fName) as f:
        l = (i.strip() for i in f.readlines())
    return l

def getValues(line):
    split = line.split()
    ox, oy = split[2].split(',')
    oy = oy[:-1]
    sx, sy = split[3].split('x')
    return int(ox), int(oy),int(sx),int(sy)


def calculateXY(ox, oy, sx, sy):
    xy = []
    for x in range(ox+1 , ox+sx+1):
        for y in range(oy+1 , oy+sy+1):
            xy.append((x,y))
    return xy

def puzzle1(l):
    #1386 @ 451,547: 25x15
    covered = set()
    overlap = set()
    for line in l:
        res = calculateXY(*getValues(line))
        for p in res:
            if p in covered:
                overlap.add(p)
            else:
                covered.add(p)
    print(len(overlap))


def puzzle2(l):
    values = []
    for line in l:
        values.append(getValues(line))

    covered = collections.defaultdict(list)
    sizes = []
    for i, (ox,oy,sx,sy) in enumerate(values):
        n = 0
        for x in range(ox+1 , ox+sx+1):
            for y in range(oy+1 , oy+sy+1):
                n+=1
                covered[(x,y)].append(i)
        sizes.append(n)
    counter = collections.Counter([v[0] for v in covered.values() if len(v)==1])
    for k,v in counter.items():
        if sizes[k] == v:
            print(l[k])
            break


if __name__ == '__main__':
    # puzzle1(readIn("d:/Sandbox/advent/2018/input3Test"))
    puzzle1(readIn())
    # puzzle2(list(readIn("d:/Sandbox/advent/2018/input3Test")))
    puzzle2(list(readIn()))
