from settings import *
import random
import sys
import time
import os


# check for initializing errors
check_errors = (pygame.init())
if (check_errors[1] > 0):
    print "(!) Had {0} initializing errors,\nexiting...".format(check_errors[1])
    sys.exit(-1)
else:
    print "(+) Pygame successfully initialized."

# Play Surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

fpsController = pygame.time.Clock()

# Declaring a sprite group
all_sprites = pygame.sprite.Group()

# Setting up assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# making a ball class using sprite


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "flyFly1.png")).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.y += 10
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = 0


# a ball object and adding it to sprite
ball = Ball()
all_sprites.add(ball)

while True:
    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    screen.fill(lblue)
    fpsController.tick(FPS)
    # update
    all_sprites.update()
    # draw
    all_sprites.draw(screen)

    pygame.display.flip()
