import pygame
import time
import random

speed = 15
width = 720
height = 480

colors = {
    "black": pygame.Color(0, 0, 0),
    "white": pygame.Color(255, 255, 255),
    "red": pygame.Color(255, 0, 0),
    "green": pygame.Color(0, 255, 0),
    "blue": pygame.Color(0, 0, 255)
}

pygame.init()
pygame.display.set_caption('Zmeyka')
game_surface = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

snake_pos = [100, 50]
snake_parts = [[100, 50], [90, 50], [80, 50], [70, 50]]
fruit_pos = [random.randrange(1, (width // 10)) * 10,
             random.randrange(1, (height // 10)) * 10]
fruit_spawned = True

current_direction = 'RIGHT'
next_direction = current_direction
score = 0

def display_score(choice, color, font_name, font_size):
    font = pygame.font.SysFont(font_name, font_size)
    score_surface = font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_surface.blit(score_surface, score_rect)

def end_game():
    font = pygame.font.SysFont('times new roman', 50)
    end_surface = font.render('Your Score: ' + str(score), True, colors["red"])
    end_rect = end_surface.get_rect()
    end_rect.midtop = (width / 2, height / 4)
    game_surface.blit(end_surface, end_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                next_direction = 'UP'
            if event.key == pygame.K_DOWN:
                next_direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                next_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                next_direction = 'RIGHT'

    
    if next_direction == 'UP' and current_direction != 'DOWN':
        current_direction = 'UP'
    if next_direction == 'DOWN' and current_direction != 'UP':
        current_direction = 'DOWN'
    if next_direction == 'LEFT' and current_direction != 'RIGHT':
        current_direction = 'LEFT'
    if next_direction == 'RIGHT' and current_direction != 'LEFT':
        current_direction = 'RIGHT'

   
    if current_direction == 'UP':
        snake_pos[1] -= 10
    if current_direction == 'DOWN':
        snake_pos[1] += 10
    if current_direction == 'LEFT':
        snake_pos[0] -= 10
    if current_direction == 'RIGHT':
        snake_pos[0] += 10

    snake_parts.insert(0, list(snake_pos))
    
  
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 10
        fruit_spawned = False
    else:
        snake_parts.pop()

   
    if not fruit_spawned:
        fruit_pos = [random.randrange(1, (width // 10)) * 10,
                      random.randrange(1, (height // 10)) * 10]
        fruit_spawned = True

    game_surface.fill(colors["black"])


    for segment in snake_parts:
        pygame.draw.rect(game_surface, colors["green"],
                         pygame.Rect(segment[0], segment[1], 10, 10))
    
    pygame.draw.rect(game_surface, colors["white"], pygame.Rect(
        fruit_pos[0], fruit_pos[1], 10, 10))
        
    if snake_pos[0] < 0 or snake_pos[0] > width - 10 or \
       snake_pos[1] < 0 or snake_pos[1] > height - 10:
        end_game()

    for segment in snake_parts[1:]:
        if snake_pos[0] == segment[0] and snake_pos[1] == segment[1]:
            end_game()

    display_score(1, colors["white"], 'times new roman', 20)

    pygame.display.update()

    clock.tick(speed)