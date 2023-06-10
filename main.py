import pygame, sys
from pygame.locals import QUIT

#initialisation
pygame.init()
#screen
DISPLAYSURF = pygame.display.set_mode((400, 300))
DISPLAYCAPTION = pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("556435.png")
DISPLAYICON = pygame.display.set_icon(icon)

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False

    pygame.display.update()