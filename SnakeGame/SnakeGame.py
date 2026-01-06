# -*- coding: utf-8 -*-
"""
Created on Fri Feb 02 18:03:27 2018

@author: Tauheed Ahmad
"""

import pygame
import sys
import random
import time

# check for initializing errors
check_errors = (pygame.init())
if (check_errors[1] > 0):
    print("(!) Had {0} initializing errors,\nexiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame successfully initialized.")

# Play Surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake Game")

# Colors
blue = pygame.Color(0, 0, 255)  # ScoreBack
red = pygame.Color(255, 0, 0)  # Gameover
green = pygame.Color(0, 255, 0)  # Snake
black = pygame.Color(0, 0, 0)  # Score
white = pygame.Color(255, 255, 255)  # Background
brown = pygame.Color(165, 42, 42)  # Food

# FPS controller
fpsController = pygame.time.Clock()

# Important Variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10 + 20]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

score = 0
best = 0
fps = 1
0
# GameOver function


def gameOver():

    globals
    myfont = pygame.font.SysFont('comicsansms', 72)
    GOSurf = myfont.render('Game Over!', True, red)
    GORect = GOSurf.get_rect()
    GORect.midtop = (360, 15)
    playSurface.blit(GOSurf, GORect)

    showScore(2, 1)
    pygame.display.flip()  # to update the window
#
#    while True:
#         for event in pygame.event.get():
#                if event.type == pygame.QUIT:
#                    pygame.quit()
#                    sys.exit()
#                elif event.type == pygame.KEYDOWN:
#                    if event.key == pygame.K_SPACE:
#                        snakePos = [100,50]
#                        snakeBody = [[100,50],[90,50],[80,50]]
#                        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10+20]
#                        foodSpawn = True
#                        direction = 'RIGHT'
#                        changeto = direction
#                        score = 0
#                        pygame.display.flip()#to update the window
#                        return 1
#                    if event.key == pygame.K_ESCAPE:
#                        pygame.event.post(pygame.event.Event(pygame.QUIT))
#
#
    time.sleep(3)
    pygame.quit()  # pygame exit
    sys.exit()  # console exit


def showScore(choice, GOflag):

    pygame.display.flip()  # to update the window

    global best, score
    if score > best and GOflag == 1:
        best = score
        choice = 3

    if choice == 1:
        myfont = pygame.font.SysFont('arial', 12)
        sSurf = myfont.render('SCORE : {0}       BEST : {1}'.format(score, best), True, white)
        sRect = sSurf.get_rect()
        sRect.midtop = (60, 12)
        playSurface.blit(sSurf, sRect)
    elif choice == 2:
        myfont = pygame.font.SysFont('arial', 30)
        sSurf = myfont.render('SCORE : {0}       BEST : {1}'.format(score, best), True, red)
        sRect = sSurf.get_rect()
        sRect.midtop = (360, 120)
        playSurface.blit(sSurf, sRect)
    else:
        myfont = pygame.font.SysFont('arial', 40)
        sSurf = myfont.render('NEW BEST : {0}'.format(best), True, red)
        sRect = sSurf.get_rect()
        sRect.midtop = (360, 120)
        playSurface.blit(sSurf, sRect)


# MAIN PROGRAM
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Validation of direction
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'

    # Direction changing
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # Hiting same body condition
    if snakeBody.count(snakePos) >= 1:
        if gameOver() == 1:
            continue

    # SnakeBody mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        foodSpawn = False
        score += 10
        fps += 1
    else:
        snakeBody.pop()

    # Food Spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10 + 20]
        foodSpawn = True

    # Setting background
    playSurface.fill(white)
    pygame.draw.rect(playSurface, blue, pygame.Rect(0, 0, 720, 30))

    # Drawing Snake & Food
    for pos in snakeBody:
        pygame.draw.circle(playSurface, green, (pos[0], pos[1]), 5)

    pygame.draw.circle(playSurface, brown, (foodPos[0], foodPos[1]), 5)

    # Boundary condition
    if snakePos[0] <= 0 or snakePos[0] >= 720 or snakePos[1] <= 30 or snakePos[1] >= 460:
        gameOver()

    showScore(1, 0)
    pygame.display.flip()  # to update the window
    fpsController.tick(fps)
