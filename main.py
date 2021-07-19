import pygame
import sys
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
length = 1
snake = [(x, y)]

dx, dy = 0, 0

fps = 60
score = 0
speed_count, snake_speed = 0, 10

pygame.init()

surface = pygame.display.set_mode((RES, RES))
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
img = pygame.image.load('1.jpg').convert()


def close_game():
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()


while True:
    surface.blit(img, (0, 0))
    [pygame.draw.rect(surface, pygame.Color('green'), (i, j, SIZE-1, SIZE-1)) for i, j in snake]
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))
    pygame.display.flip()
    clock.tick()
    close_game()

