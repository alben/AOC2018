import collections

def readIn():
    l = []
    with open("d:/Sandbox/advent/2018/input2") as f:
        l = (i.strip() for i in f.readlines())
    return l




def puzzle1(l):
    dos = 0
    tres = 0
    for line in l:
        c = collections.Counter(line)
        if any(i==2 for i in c.values()): dos+=1
        if any(i==3 for i in c.values()): tres+=1

    print(dos * tres)
        

def checkLines(s1, s2):
    total = False
    letters = []
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            letters.append(s1[i])
        elif total:
            return False
        else:
            total = True
    print('----------------', ''.join(letters))
    return True

def puzzle2(l):
    reducedLines = [set(line) for line in l]
    for i, _ in enumerate(reducedLines):
        for n, _ in enumerate(reducedLines[i+1:], i+1):
            if checkLines(l[i], l[n]): 
                break
        else:
            continue
        break

if __name__ == '__main__':
    t1 = [+3, +3, +4, -2, -4]
    puzzle1(readIn())
    # puzzle2(t1)
    puzzle2(list(readIn()))
