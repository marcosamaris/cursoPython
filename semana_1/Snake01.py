import pygame, random
from pygame.locals import *


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

TAM = 512

def on_grid_random(labirinto):
    x = random.randrange(0, 500, 10)
    y = random.randrange(0, 500, 10)
    if labirinto.get_at((x,y)) != Color('black'):
        return (x,y)
    else:
        return (50,400)

def collision(pos1, pos2):
    return (pos1[0]==pos2[0]) and (pos1[1] == pos2[1])

pygame.init()
screen = pygame.display.set_mode((TAM,TAM))

snake = [(300,300), (310, 300), (320, 300)]
snake_kin = pygame.Surface((10,10))
snake_kin.fill((200, 0, 0))

labirinto=pygame.image.load('labirinto.png')
#labirinto=pygame.transform.scale(labirinto, (TAM,TAM))

apple = pygame.Surface((10,10))
apple.fill((0, 255, 0))
apple_pos = on_grid_random(labirinto)



background = pygame.Surface((TAM,TAM))
background.fill((255,255,255))

my_direction = -1

clock = pygame.time.Clock()

my_direction=LEFT
while True:
    clock.tick(20)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN   
            
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT

            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos=on_grid_random(labirinto)
        snake.append((0,0))

    for i in range(len(snake)-1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1]-10)
        

    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1]+10)
        
        
    if my_direction == LEFT:
        snake[0] = (snake[0][0]-10, snake[0][1])
        
        
    if my_direction == RIGHT:
        snake[0] = (snake[0][0]+10, snake[0][1])
        
        
    if labirinto.get_at((snake[0][0]+2, snake[0][1]+2)) == Color('black'):
        pygame.quit()

    

    screen.blit(background, (0,0))
    screen.blit(labirinto, (0,0))
    screen.blit(apple, apple_pos)



    for pos in snake:
        screen.blit(snake_kin, pos)
    pygame.display.update()