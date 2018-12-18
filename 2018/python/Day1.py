import itertools

def readIn():
    l = []
    with open("d:/Sandbox/advent/2018/input1") as f:
        l = (int(i.strip()) for i in f.readlines())
    return l
def puzzle1(l):
    print(sum(l))

def puzzle2(l):
    fqs = [0,]
    fq = 0
    for i in l:
        fq = fq + i
        if fq in fqs:
            break
        fqs.append(fq)
    else:
        for i in itertools.cycle(l):
            fq = fq + i
            if fq in fqs:
                print('...br', i)    
                break
    print(fq)

if __name__ == '__main__':
    t1 = [+3, +3, +4, -2, -4]
    puzzle1(readIn())
    # puzzle2(t1)
    puzzle2(list(readIn()))
