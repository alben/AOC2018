import collections
import itertools
import numpy as np

def readIn(fName="d:/Sandbox/advent/2018/input6"):
    l = []

    with open(fName) as f:
        l = (i.strip() for i in f.readlines())
    return l

def get_coor(l):
    return [tuple(map(lambda x: int(x), i.split(','))) for i in l]

def get_closest(x, y, coor):
    res = []
    for c in coor:
        t = abs(x - c[0]) + abs(x - c[1])
        res.append(t)
    max_d = 0
    max_i = -1
    for i, d in enumerate(res):
        if d > max_d:
            max_d = d
            max_i = i
        elif d == max_d:
            max_i = -1
    return max_i, max_d

def get_max_size(coor):
    x = max([c[0] for c in coor])
    y = max([c[1] for c in coor])
    return x+1, y+1

def puzzle1(coor):
    x, y = get_max_size(coor)
    matrix= np.empty((x,y))
    for i in range(x):
        for n in range(y):
            cl_i, cl_d = get_closest(x, y, coor)
            matrix[i][n] = cl_i
    pass
    print(matrix)

def puzzle2(l):
    pass


if __name__ == '__main__':
    puzzle1(get_coor(readIn("d:/Sandbox/advent/2018/input6Test")))
    # puzzle1(readIn())
    puzzle2(list(readIn("d:/Sandbox/advent/2018/input6Test")))
    # puzzle2(list(readIn()))
