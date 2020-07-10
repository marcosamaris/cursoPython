import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((300,300))

back = pygame.Surface((300,300))
back.fill( (200, 0, 0) )

lob = []
lob.append( pygame.image.load("imagens/frame-1.gif") )
lob.append( pygame.image.load("imagens/frame-2.gif") )
lob.append( pygame.image.load("imagens/frame-3.gif") )
lob.append( pygame.image.load("imagens/frame-4.gif") )
lob.append( pygame.image.load("imagens/frame-5.gif") )
lob.append( pygame.image.load("imagens/frame-6.gif") )
lob.append( pygame.image.load("imagens/frame-7.gif") )
lob.append( pygame.image.load("imagens/frame-8.gif") )

clock = pygame.time.Clock()
time = 10

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    screen.blit(lob[0], (0,0))
    pygame.display.update()
    screen.blit(back, (0,0))
    clock.tick(time)

    screen.blit(lob[1], (0,0))
    pygame.display.update()
    screen.blit(back, (0,0))
    clock.tick(time)

    screen.blit(lob[2], (0,0))
    pygame.display.update()
    screen.blit(back, (0,0))
    clock.tick(time)

    screen.blit(lob[3], (0,0))
    pygame.display.update()
    screen.blit(back, (0,0))
    clock.tick(time)

    screen.blit(lob[4], (0,0))
    pygame.display.update()
    screen.blit(back, (0,0))
    clock.tick(time)

    screen.blit(lob[5], (0,0))
    pygame.display.update()
    screen.blit(back, (0,0))
    clock.tick(time)

    screen.blit(lob[6], (0,0))
    pygame.display.update()
    screen.blit(back, (0,0))
    clock.tick(time)

    screen.blit(lob[7], (0,0))
    pygame.display.update()
    screen.blit(back, (0,0))
    clock.tick(time)