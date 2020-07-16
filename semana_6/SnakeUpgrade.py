import pygame
import random
from pygame.locals import *

CIMA=0
BAIXO=1
ESQUERDA=2
DIREITA=3

def level1():
    pygame.draw.line(tela, (0,0,0), [10,10], [10,590], 10)
    pygame.draw.line(tela, (0,0,0), [590,10], [590,590], 10)
    pygame.draw.line(tela, (0,0,0), [10,10], [590,10], 10)
    pygame.draw.line(tela, (0,0,0), [10,590], [590,590], 10)

def level2():
    pygame.draw.rect(tela, (0,0,0), [100,10, 10, 200], 5)
    pygame.draw.rect(tela, (0,0,0), [200,10, 10, 200], 5)
    pygame.draw.rect(tela, (0,0,0), [300,10, 10, 200], 5)
    pygame.draw.rect(tela, (0,0,0), [400,10, 10, 200], 5)
    pygame.draw.rect(tela, (0,0,0), [500,10, 10, 200], 5)

    pygame.draw.rect(tela, (0,0,0), [100,390, 10, 200], 5)
    pygame.draw.rect(tela, (0,0,0), [200,390, 10, 200], 5)
    pygame.draw.rect(tela, (0,0,0), [300,390, 10, 200], 5)
    pygame.draw.rect(tela, (0,0,0), [400,390, 10, 200], 5)
    pygame.draw.rect(tela, (0,0,0), [500,390, 10, 200], 5)

def level3():
    pygame.draw.rect(tela, (0,0,0), [100,300, 400,20], 10)

def next_level(snake):
    if len(snake) <= 10:
        level1()
    elif len(snake) > 10 and len(snake) <= 15:
        level2()
    elif len(snake) > 15:
        level3()



def on_grid_random():
    x = random.randrange(0, 500, 10)
    y = random.randrange(0, 500, 10)

    while tela.get_at((x,y)) == (0,0,0):
        x = random.randrange(0, 500, 10)
        y = random.randrange(0, 500, 10)

    return (x,y)
    

def colission(pos1, pos2):
    return (pos1[0] == pos2[0]) and (pos1[1] == pos2[1])

pygame.init()

pygame.display.set_caption('Jogo da cobrinha')
tela=pygame.display.set_mode((600,600))

tela_de_fundo = pygame.Surface((600, 600))
tela_de_fundo.fill((0,255,0))


snake = [(300, 300), (310,300), (320,300)]
snake_cor = pygame.Surface((10,10))
snake_cor.fill((255,0,255))

apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_pos = (250, 300)


direcao = -1

clock = pygame.time.Clock()
direcao = DIREITA
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP and direcao != BAIXO:
                direcao = CIMA
            if event.key == K_DOWN and direcao != CIMA:
                direcao = BAIXO
            if event.key == K_LEFT and direcao != DIREITA:
                direcao = ESQUERDA
            if event.key == K_RIGHT and direcao != ESQUERDA:
                direcao = DIREITA

    if direcao == CIMA:
        snake[0] = (snake[0][0], snake[0][1]-10)
    if direcao == BAIXO:
        snake[0] = (snake[0][0], snake[0][1]+10)
    if direcao == ESQUERDA:
        snake[0] = (snake[0][0]-10, snake[0][1])
    if direcao == DIREITA:
        snake[0] = (snake[0][0]+10, snake[0][1])

    for i in range(len(snake)-1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])   
    
    if colission(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))

    tela.blit(tela_de_fundo, (0,0))
    tela.blit(apple, apple_pos)

    for pos in snake:
        tela.blit(snake_cor, pos)
    
    next_level(snake)

    if tela.get_at(snake[0]) == (0,0,0):
        pygame.quit()

    pygame.display.update()