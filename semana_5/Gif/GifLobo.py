import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((300,300))

back = pygame.Surface((300,300))
back.fill( (200, 0, 0) )

lob = []
for i in range(1, 9):
    lob.append( pygame.image.load("imagens/frame-{}.gif".format(i)) ) 

clock = pygame.time.Clock()
time = 10

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    for i in lob:
        screen.blit(i, (0,0))
        pygame.display.update()
        screen.blit(back, (0,0))
        clock.tick(time)