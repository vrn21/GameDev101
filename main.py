import pygame, sys
from pygame.locals import QUIT
import random

#initialisation
pygame.init()

#screen and images
screen = pygame.display.set_mode((800, 600))
caption = pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("556435.png")
displayicon = pygame.display.set_icon(icon)
screenbackground = pygame.image.load("430122-PEB23Y-66 (1).jpg")

#player
playimg = pygame.image.load("space-invaders.png")
playerx = 370
playery = 380
playerx_change = 0

#enemy
enemyicon = pygame.image.load("alien.png")
enemyx = random.randint(0, 800)
enemyy = random.randint(0, 150)
enemyx_change = 0.3
enemyy_change = 40

#bullet
bulleticon = pygame.image.load("bullet.png")
bulletx = 0
bullety = 380
bulletx_change = 0
bullety_change = 40
bullet_state = "ready"


def player(x, y):
    screen.blit(playimg, (x, y))


def enemy(x, y):
    screen.blit(enemyicon, (x, y))


def fire_bullet(x, y):

    screen.blit(bulleticon, (x + 16, y + 10))


#game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(screenbackground, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #keystroke is pressed
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerx_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3
            if event.key == pygame.K_SPACE:
                fire_bullet(playerx, bullety)
    #Release the keystroke
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    playerx += playerx_change
    enemyx += enemyx_change
    enemyy += enemyy_change

    #boundaries of user and enemy
    if playerx <= 0:
        playerx_change = 0.3
    elif playerx <= 736:
        playerx_change = -0.3

    if enemyx <= 0:
        enemyx_change = 0.3
    elif enemyx <= 736:
        enemyx_change = -0.3
    #bullet movements
    if bullet_state == "fire":
        fire_bullet(playerx, bullety)
        bullety -= bullety_change

    player(playerx, playery)
    enemy(enemyx, enemyy)
    fire_bullet(playerx, playery)
    pygame.display.update()
