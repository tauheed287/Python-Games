from settings import *
from sprites import *
import pygame
import random
import sys
import time
import os


class Game():

    def __init__(self):
        check_errors = (pygame.init())
        if (check_errors[1] > 0):
            print("(!) Had {0} initializing errors,\nexiting...".format(check_errors[1]))
            sys.exit(-1)
        else:
            print("(+) Pygame successfully initialized.")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.fpsController = pygame.time.Clock()
        self.running = True

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        p1 = Platform(0, HEIGHT - 20, WIDTH, 20)
        self.player = Player()
        self.all_sprites.add(p1)
        self.platforms.add(p1)

        p2 = Platform(WIDTH / 2, HEIGHT * 3 / 4, 40, 20)
        self.all_sprites.add(p2)
        self.platforms.add(p2)

        self.all_sprites.add(self.player)

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draws()
            pygame.display.flip()
            self.fpsController.tick(FPS)

    def update(self):
        self.all_sprites.update()

        # Stop only if therr is a platform in there
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("event")
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self.player.jump()
                    # pygame.event.post(pygame.event.Event(pygame.QUIT))

    def draws(self):
        self.screen.fill(white)
        self.all_sprites.draw(self.screen)

    def showStartScreen(self):
        pass

    def showGameOver(self):
        pass


g = Game()
g.showStartScreen()
while g.running:
    print("hello")
    g.new()
    g.run()
    g.showGameOver()
pygame.quit()
