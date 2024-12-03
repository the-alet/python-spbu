from math import *
from random import *
from os import system
import pygame
from time import sleep

chance = 20

WIDTH, HEIGHT = 50, 50#map(int, input().split())

def visualize_astar(FIELD, scale=10):
    width, height = WIDTH * scale, HEIGHT * scale
    null = Node(-1, -1, True)
    root, dest = null, null
    running = True
    way = []
    poss = []
    
    pygame.init()
    pygame.display.set_caption('A*')
    game_surface = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    colors = {
        "black": pygame.Color(0, 0, 0),
        "white": pygame.Color(255, 255, 255),
        "red": pygame.Color(255, 0, 0),
        "green": pygame.Color(0, 255, 0),
        "blue": pygame.Color(0, 0, 255)
    }

    while running:
        # Draw the grid
        game_surface.fill(colors["black"])
        for y in FIELD:
            for f in y:
                color = colors["white"] if f.isWall else colors["black"]
                pygame.draw.rect(game_surface, color, (f.x * scale, f.y * scale, scale, scale))
        pygame.display.flip()


        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = tuple(map(int, pygame.mouse.get_pos()))
                res = (pos[0] < 0 and pos[0] >= WIDTH * scale and pos[1] < 0 and pos[1] >= HEIGHT * scale)
                if res:
                  poss.append(pos)
                if len(poss) > 2: poss = poss[1:]
        if len(poss) == 2:
            root = FIELD[poss[0][1]//scale][pos[0][0]//scale]
            dest = FIELD[pos[1][1]//scale][pos[1][0]//scale]
            wayF = buildWayField(FIELD, root)
            FIELD = copyDist(FIELD, wayF)
            way = getWay(FIELD, root, dest)
        rway = [way[i] for i in range(len(way) - 1, -1, -1)]
        way = rway
        if way == []:
            continue
        # Draw the path
        pygame.draw.rect(game_surface, colors["green"], (way[0].x * scale, way[0].y * scale, scale, scale))
        for n in way[1:-1]:
            pygame.draw.rect(game_surface, colors["red"], (n.x * scale, n.y * scale, scale, scale))
            sleep(0.08)
            pygame.display.flip()

        # Highlight start and destination
        pygame.draw.rect(game_surface, colors["blue"], (way[-1].x * scale, way[-1].y * scale, scale, scale))

        for n in way:
            pygame.draw.rect(game_surface, colors["black"], (n.x * scale, n.y * scale, scale, scale))
            sleep(0.08)
            pygame.display.flip()
        way = []
        
        clock.tick(10)

    # pygame.quit()

# Call the visualization function after computing the path
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
    FIELD = fieldInit(WIDTH, HEIGHT)
    visualize_astar(FIELD)
