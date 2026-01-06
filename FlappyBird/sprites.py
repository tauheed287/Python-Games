from settings import *
import os
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        # setting up assets folder
        pygame.sprite.Sprite.__init__(self)

        # image directory
        self.game_folder = os.path.dirname(__file__)
        self.img_folder = os.path.join(self.game_folder, "img")

        self.image = pygame.image.load(os.path.join(self.img_folder, "1.png")).convert()
        self.image.set_colorkey(red)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 50, HEIGHT / 2)

        # variables used for changing image
        self.temp = 0
        self.temp1 = 0

        self.pos = vec(WIDTH - 50, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def change_image(self):
        if self.temp > 100:
            self.temp = 0

        self.temp += 1

        if self.temp % 10 == 0:
            self.temp1 += 1

        if self.temp1 % 2 == 0:
            self.image = pygame.image.load(os.path.join(self.img_folder, "aa (1).jpg")).convert()  # THIS IMAGE SHOULD CONTAIN IN THE SAME LOACTION AS MENTIONED
        else:                                                                                       # IN THE LOCATION DIRECTORY IN INIT FUNCTION OF PLAYER
            self.image = pygame.image.load(os.path.join(self.img_folder, "aa (2).jpg")).convert()

        self.image.set_colorkey(black)

    def jump(self):
        self.vel.y = PLAYER_JUMP

    def update(self):

        self.change_image()

        self.acc = vec(0, PLAYER_GRAVITY)

        # this code is for stimulating player through arrow keys
        """keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC

        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        if keys[pygame.K_DOWN]:
            self.acc.y = PLAYER_ACC

        if keys[pygame.K_UP]:
            self.acc.y = -PLAYER_ACC
        """
        # Applying PLAYER_FRICTION
        self.acc.x += self.vel.x * PLAYER_FRICTION

        # Laws of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        """
        # Boudary Conditions
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        """
        self.rect.midbottom = self.pos


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(brown)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class U_pillar(pygame.sprite.Sprite):
    # the "h" parameter is height of upper pillar upto gap
    # "w" is the width of the pillar
    # pillar is coming from left to right

    def __init__(self, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(green)
        self.rect = self.image.get_rect(topleft=(-w, 0))

    def update(self):
        self.rect.x += PILLAR_VEL


class L_pillar(pygame.sprite.Sprite):
    def __init__(self, w, h, gap):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(green)
        self.rect = self.image.get_rect(bottomleft=(-w, HEIGHT - 20))

    def update(self):
        self.rect.x += PILLAR_VEL


class Create_Pillar():
    def __init__(self, w, h, gap, all_sprites, pillar):

        self.upper = U_pillar(w, h)
        all_sprites.add(self.upper)
        pillar.add(self.upper)

        self.lower = L_pillar(w, HEIGHT - (h + gap), gap)
        all_sprites.add(self.lower)
        pillar.add(self.lower)
