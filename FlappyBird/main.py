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

        # pygame.mixer.init()
        # self.flysound = pygame.mixer.Sound("sound\point.wav")

    def new(self):
        self.score = 0
        self.pillar_flag = 1  # this flag is used to create second pillar when first reached to middle
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()  # the platform group is defined separately because to use it as collision parameter
        self.pillar = pygame.sprite.Group()

        self.player = Player()

        # creating first pillar
        self.p1 = self.p2 = Create_Pillar(PILLAR_WIDTH, random.randrange(20, WIDTH - GAP - 20), GAP, self.all_sprites, self.pillar)
        self.p2_scoreflag = 1  # this is used to ensure to increment the score only once when surpassing pillar 2

        base = Platform(0, HEIGHT - 20, WIDTH, 20)  # the red platform
        self.all_sprites.add(base)
        self.platforms.add(base)
        self.all_sprites.add(self.player)

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draws()
            self.showScore()
            pygame.display.flip()
            self.fpsController.tick(FPS)

    def update(self):
        if self.playing == False:
            return
        self.all_sprites.update()

        # this part will run only once
        if self.p2.lower.rect.x > WIDTH / 2 - 25 and self.pillar_flag == 1:
            self.p1 = Create_Pillar(PILLAR_WIDTH, random.randrange(20, WIDTH - GAP - 20), GAP, self.all_sprites, self.pillar)
            self.p1_scoreflag = 1  # this is used to ensure to increment the score only once when surpassing pillar 2
            self.pillar_flag = 0
        #==================================#

        # assigning the pillar alternativly to p1 and p2 whenver they go out of screen to keep it balanced
        if self.p1.lower.rect.x > WIDTH:
            self.p1 = Create_Pillar(PILLAR_WIDTH, random.randrange(20, WIDTH - GAP - 20), GAP, self.all_sprites, self.pillar)
            self.p1_scoreflag = 1

        if self.p2.lower.rect.x > WIDTH:
            self.p2 = Create_Pillar(PILLAR_WIDTH, random.randrange(20, WIDTH - GAP - 20), GAP, self.all_sprites, self.pillar)
            self.p2_scoreflag = 1
        #==================================#

        # Incrementing Score
        if self.p1.lower.rect.x > self.player.rect.x and self.p1_scoreflag == 1:
            self.score += 1
            self.p1_scoreflag = 0

        if self.p2.lower.rect.x > self.player.rect.x and self.p2_scoreflag == 1:
            self.score += 1
            self.p2_scoreflag = 0

        pygame.display.flip()
        #===================================#

        # show gameover when hit by the platform
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.playing = False
                return

        # show gameover when hit with the pillar
        hits = pygame.sprite.spritecollide(self.player, self.pillar, False)
        if hits:
            self.player.vel.y = 0
            self.playing = False
            return

    def events(self):
        if self.playing == False:
            return
        # getting inputs
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
                    #self.flysound.play()
                    self.player.jump()

    def draws(self):
        if self.playing == False:
            return
        self.screen.fill(lblue)
        self.all_sprites.draw(self.screen)

    def showScore(self):
        if self.playing == False:
            return
        # showing the score continuosly
        myfont = pygame.font.SysFont('arial', 12)
        sSurf = myfont.render('SCORE : {0} '.format(self.score), True, white)
        sRect = sSurf.get_rect()
        sRect.midtop = (WIDTH - 50, HEIGHT - 18)
        self.screen.blit(sSurf, sRect)
        pass  # IN THE LOCATION DIRECTORY IN INIT FUNCTION OF PLAYER

    def showStartScreen(self):
        self.screen.fill(purple)
        self.draw_text(TITLE, 48, white, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Space to jump", 22, white, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press any key to play", 22, white, WIDTH / 2, HEIGHT * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()

    def showGameOver(self):

        # game over/continue
        if self.running == False:
            return
        self.screen.fill(purple)
        self.draw_text("GAME OVER", 48, white, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, white, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play again", 22, white, WIDTH / 2, HEIGHT * 3 / 4)
        pygame.display.flip()
        time.sleep(1)
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.fpsController.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP and event.key != pygame.K_ESCAPE:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('arial', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()
g.showStartScreen()

while g.running:
    g.new()
    g.run()
    time.sleep(1)
    g.showGameOver()
pygame.quit()
