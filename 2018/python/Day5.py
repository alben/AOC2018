def readIn(fName="d:/Sandbox/advent/2018/input5"):
    l = []
    with open(fName) as f:
        l = (i.strip() for i in f.readlines())
    return l

def reduce(sec):
    i = 0
    res = sec
    offset = 0
    while i < len(sec) - 1:
        if sec[i] == sec[i+1]:
            pass
        elif sec[i].islower():
            if sec[i].upper() == sec[i + 1]:
                res = res[:i-offset] + res[i+2-offset:]  
                offset +=2
                i+=2
                continue
        elif sec[i].lower() == sec[i + 1]:
            res = res[:i-offset] + res[i+2-offset:]  
            offset +=2
            i+=2
            continue
        i+=1
        continue
    return res

def puzzle1(l):
    total = len(l)
    while True:
        l = reduce(l)
        # print(l)
        if len(l) < total:
            total = len(l)
        else: break
    print(total)
    return total

def puzzle2(l):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    totals = []
    for letter in abc:
        t = l.replace(letter, '').replace(letter.upper(), '')
        totals.append(puzzle1(t))
    print(min(totals))

if __name__ == '__main__':
    # puzzle1("dabAcCaCBAcCcaDA")
    # puzzle1(next(readIn()))
    puzzle2(next(readIn()))