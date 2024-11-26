from math import *
import pygame
import random
from pygame.locals import *
from pygameZoom import PygameZoom

# Константы
WIDTH, HEIGHT = 150, 150
SCALE = 5
WINDOW_WIDTH, WINDOW_HEIGHT = WIDTH * SCALE, HEIGHT * SCALE
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
FPS = 2

# Направления движения
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # вниз, вправо, вверх, влево


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Sobaka")
        self.clock = pygame.time.Clock()
        self.running = True

        self.non_edge_positions = []
        for y in (10, HEIGHT - 10):
            for x in (10, WIDTH - 10):
                self.non_edge_positions.append((x,y))


        # Позиция синей точки
        self.dog_pos = [WIDTH // 2, HEIGHT // 2]
        self.safe_pos = [WIDTH // 2, HEIGHT // 2]
        self.red_dot_pos = [0, 0]
        self.resque_fl = 0
        self.trail = set()  # Множество для хранения следа

        # Создаем объект Zoom
        self.zoom = PygameZoom(WINDOW_WIDTH, WINDOW_HEIGHT)



    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.resque()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

    def update(self):
        if self.resque_fl: return
        # Случайное направление
        direction = random.choice(DIRECTIONS)
        new_pos = (self.dog_pos[0] + direction[0], self.dog_pos[1] + direction[1])
        while new_pos in self.trail:
            direction = random.choice(DIRECTIONS)
            new_pos = (self.dog_pos[0] + direction[0], self.dog_pos[1] + direction[1])
            if self.is_stuck(self.dog_pos):
                self.resque_prepare()
                return

        # Проверка выхода за границы
        if new_pos[0] < 0 or new_pos[0] >= WIDTH or new_pos[1] < 0 or new_pos[1] >= HEIGHT:
            self.running = False  # Игра заканчивается

        # Проверка на тупик
        if tuple(new_pos) in self.trail and self.is_stuck(new_pos): self.resque_prepare()
        else:
            # Обновляем позицию синей точки и добавляем в след
            self.dog_pos = new_pos
            self.trail.add(tuple(self.dog_pos))

    def is_stuck(self, pos):
        for direction in DIRECTIONS:
            neighbour = (pos[0] + direction[0], pos[1] + direction[1])
            if neighbour not in self.trail:
                return False
        return True

    def resque_prepare(self):
        self.resque_fl = 1
        self.red_dot_pos = [0 if 2 * x < WIDTH else WIDTH - x, self.dog_pos[1]]
        
        # Выбираем случайную позицию не на краю поля
        p = random.choice(self.non_edge_positions)
        while p in self.trail or self.is_stuck(p):
            p = random.choice(self.non_edge_positions)
        # Перемещаем синюю точку на случайное место не на краю поля
        self.safe_pos = list(p)        

    def rescue(self):
        if not self.resque_fl: return

        if self.red_dot_pos[0] == self.safe_pos[0] and self.red_dot_pos[1] == self.safe_pos[1]:
            self.resque_fl = 0 
            self.trail = set()
            self.dog_pos = self.safe_pos

        dx, dy = self.safe_pos[0] - self.red_dot_pos[0], self.safe_pos[1] - self.red_dot_pos[1]
        if abs(dx) > abs(dy): self.red_dot_pos[0] += sign(dx)
        else: self.red_dot_pos[1] += sign(dy)
    
    def draw(self):
        # Заполняем экран черным цветом
        self.screen.fill(BLACK)

        # Рисуем след
        for pos in self.trail:
            scaled_pos = (pos[0] * SCALE, pos[1] * SCALE)
            self.screen.fill(LIGHT_BLUE, (scaled_pos[0], scaled_pos[1], SCALE, SCALE))

        # Рисуем синюю точку
        blue_scaled_pos = (self.dog_pos[0] * SCALE, self.dog_pos[1] * SCALE)
        self.screen.fill(BLUE, (blue_scaled_pos[0], blue_scaled_pos[1], SCALE, SCALE))

        if self.resque_fl:
            self.screen.fill(RED, (self.red_dot_pos[0] * SCALE, self.red_dot_pos[1] * SCALE, SCALE, SCALE))

        # Обновляем экран
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()  