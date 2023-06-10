import pygame, sys
from pygame.locals import QUIT

#initialisation
pygame.init()
#screen
screen = pygame.display.set_mode((800, 600))
caption = pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("556435.png")
displayicon = pygame.display.set_icon(icon)

#player
playimg = pygame.image.load("space-invaders.png")
playerx = 370
playery = 480


def player(x, y):
    screen.blit(playimg, (x, y))


#game loop
running = True
while running:
    screen.fill((0, 0, 0))

    player(playerx, playery)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                print("L")
            if event.type == pygame.K_RIGHT:
                print("R")
        #Release the keystroke
        if event.type == pygame.KEYUP:
            if event.type.K_LEFT or event.type.K_RIGHT:
                print("Released")

    pygame.display.update()
