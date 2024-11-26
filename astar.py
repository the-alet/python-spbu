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
        if self.x > 0 and self.x < WIDTH - 1:
            if not F[self.y][self.x - 1].isWall: self.neighbours.append(F[self.y][self.x - 1])
            if not F[self.y][self.x + 1].isWall: self.neighbours.append(F[self.y][self.x + 1])
        if self.y > 0 and self.y < HEIGHT - 1:
            if not F[self.y - 1][self.x].isWall: self.neighbours.append(F[self.y - 1][self.x])
            if not F[self.y + 1][self.x].isWall: self.neighbours.append(F[self.y + 1][self.x])
        return self.neighbours

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
    # queue = [r] + r
    
    # curr = 0
    # while curr <= len(queue):
    #     n = queue[curr].neighbours
    #     for i in range(len(n)): n[i].dist = queue[curr].dist + 1
    #     queue.extend(n)
    #     queue = list(set(queue))
    #     for i in queue: print((i.x, i.y))
    #     curr += 1

    # wayMap = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
    # for n in queue:
    #     wayMap[n.y][n.x] = n.dist

    return []#wayMap
#### TO DO ^^^^^^ 

if __name__ == "__main__":
    WIDTH, HEIGHT = map(int, input().split())

    FIELD = fieldInit(WIDTH, HEIGHT)
    
    draw(FIELD)

    root, dest = getRootDest(FIELD)

    # system("cls")

    wayMap = buildWayField(FIELD, root)

    for n in wayMap:
        print(*n)  