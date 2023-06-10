import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')


#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
          running = False
            
            
    pygame.display.update()