from math import *
from random import *
from os import system

chance = 30


class Node:
    def __init__(self, x, y, isWall):
        self.x = x
        self.y = y
        self.dist = 0
        self.isWall = isWall
        self.neighbours = []
        
    def getNeighbours(self, F):    
        if self.x < WIDTH - 1:
            if not F[self.y][self.x + 1].isWall: self.neighbours.append(F[self.y][self.x + 1])
        if self.x > 0:
            if not F[self.y][self.x - 1].isWall: self.neighbours.append(F[self.y][self.x - 1])
        if self.y < HEIGHT - 1:
            if not F[self.y + 1][self.x].isWall: self.neighbours.append(F[self.y + 1][self.x])
        if self.y > 0:
            if not F[self.y - 1][self.x].isWall: self.neighbours.append(F[self.y - 1][self.x])
        return list(set(self.neighbours))

def fieldInit(W, H):
    FIELD = [[Node(x, y, randint(0, 100) < chance) for x in range(WIDTH)] for y in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if not FIELD[y][x].isWall:
                FIELD[y][x].getNeighbours(FIELD)
    return FIELD


def draw(F):
    for n in F:
        print(*[1 if i.isWall else 0 for i in n])

def getRootDest(F):
    root_xy = list(map(int, input().split()))
    while FIELD[root_xy[1]][root_xy[0]].isWall or\
        root_xy[0] < 0 or root_xy[1] < 0 or root_xy[0] >= WIDTH or root_xy[1] >= HEIGHT:
        
        root_xy = list(map(int, input().split()))
    root = FIELD[root_xy[1]][root_xy[0]]
    
    dest_xy = list(map(int, input().split()))
    while FIELD[dest_xy[1]][dest_xy[0]].isWall or dest_xy == root_xy or\
        dest_xy[0] < 0 or dest_xy[1] < 0 or dest_xy[0] >= WIDTH or dest_xy[1] >= HEIGHT:

        dest_xy = list(map(int, input().split()))
    dest = FIELD[dest_xy[1]][dest_xy[0]]

    return root, dest

def getManhattanDist(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def buildWayField(F, r):
    wayMap = [[-1 for x in range(WIDTH)] for y in range(HEIGHT)]
    q = [r]
    wayMap[r.y][r.x] = 0
    while len(q) > 0:
        a = q[0]
        q = q[1:]
        for n in a.neighbours:
            if wayMap[n.y][n.x] == -1:
                wayMap[n.y][n.x] = wayMap[a.y][a.x] + 1
                q.append(n)

    return wayMap

def copyDist(F, wM):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            F[y][x].dist = wM[y][x]

    return F
    
def getWay(F, root, dest):
    if dest.dist == -1: return []
    q = [dest]
    while q[-1] != root:
        for n in q[-1].neighbours:
            if n.dist == q[-1].dist - 1:
                q.append(n)
                break
    return q

if __name__ == "__main__":
    WIDTH, HEIGHT = map(int, input().split())

    FIELD = fieldInit(WIDTH, HEIGHT)
    
    draw(FIELD)

    root, dest = getRootDest(FIELD)

    # system("cls")

    wayMap = buildWayField(FIELD, root)

    # for n in wayMap:
    #     for m in n:
    #         print(f'{m:>3}', end = " ")
    #     print()

    FIELD = copyDist(FIELD, wayMap)

    way = getWay(FIELD, root, dest)
    way_xy = reversed([(i.x, i.y) for i in way])
    if way == []:
        print("No way")

    print(*way_xy)