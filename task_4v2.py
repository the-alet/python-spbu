from random import *
import os
from termcolor import colored

inf = 100000


def f1(j, i, w, h):
    return 'x' if randint(1, w + h) < abs(w + h - i - j) / 2 else 'o'


def f2(j, i, w, h):
    return abs(j - w // 2) + abs(i - h // 2)


def mapGen(w, h):
    mapa = [['0' for x in range(w + 2)] for y in range(h + 2)]

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            mapa[i][j] = 'x' if randint(1, w + h) < abs(w + h - i - j) / 2 else 'o'

    mapa[h // 2][w // 2] = '*'
    return mapa, w // 2, h // 2


def mapGen1(mp, w, h, x, y):
    m = [[inf if x == 0 or y == 0 or x == w + 1 or y == h + 1 \
              else -1 if mp[y][x] == 'x' \
        else 0 for x in range(w + 2)] for y in range(h + 2)]
    for k in range(max(w, h)):
        for i in range(1, h + 1):
            for j in range(1, w + 1):
                if m[i][j] == 0:
                    m[i][j] = max(m[i + 1][j], m[i][j + 1], m[i - 1][j], m[i][j - 1]) - 1
    m[y][x] = 0
    return m


def bfs(mp, w, h, x, y):
    ways = []
    m = mapGen1(mp, w, h, x, y)
    cq = [(x, y)]
    while m[cq[-1][1]][cq[-1][0]] < inf:
        a = cq[-1]
        if m[a[1]][a[0]] < 0: continue
        n = [(a[0] - 1, a[1]), (a[0] + 1, a[1]), (a[0], a[1] - 1), (a[0], a[1] + 1)]
        mx = max(n, key=lambda v: m[v[1]][v[0]])
        # print(mx)
        if mx not in cq:
            cq.append(mx)
        else:
            cq = []
            break
    # print(cq)
    # for a in m: print(a)
    return cq


m, n = map(int, input().split())
res, x, y = 0, 0, 0
way, labMap = [], [[]]
while res == 0:
    labMap, x, y = mapGen(m, n)
    way = bfs(labMap, m, n, x, y)[1:]
    res = len(way)
#labMap, x, y = mapGen(m, n, f1)
#res, way = bfs(labMap, m, n, x, y)
os.system('cls')
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(colored(str(labMap[i][j]), 'magenta') if j == x and i == y \
                  else colored(str(labMap[i][j]), 'red') if (j, i) in way \
            else colored(str(labMap[i][j]), 'blue') if labMap[i][j] == 'x' \
            else labMap[i][j], end=' ')
    print('')
# print(way)
while len(way) > 0:
    if input():
        os.system('cls')
        labMap[y][x] = 'o'
        x, y = way[0]
        way = way[1:]
        labMap[y][x] = '*'
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                print(colored(str(labMap[i][j]), 'magenta') if j == x and i == y \
                          else colored(str(labMap[i][j]), 'red') if (j, i) in way \
                    else colored(str(labMap[i][j]), 'blue') if labMap[i][j] == 'x' \
                    else labMap[i][j], end=' ')
            print('')
