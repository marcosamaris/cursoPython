import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,600))

s = []
for i in range (0, 43):
    if i <= 9:
        s.append('frame_0{}_delay-0.04s.png'.format(i))
    else:
        s.append('frame_{}_delay-0.04s.png'.format(i))

image = []
url="/home/kalebe/Projects/Projects-in-Python/GIF/frames/"
for path in s:
    image.append(pygame.image.load(url+path))

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    for i in range(len(image)):
        screen.blit(image[i], (0,0))
        pygame.display.update()
        clock.tick(20)