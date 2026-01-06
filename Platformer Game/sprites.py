from settings import *
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.vel.y = -20

    def update(self):

        self.acc = vec(0, 1.5)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC

        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        if keys[pygame.K_DOWN]:
            self.acc.y = PLAYER_ACC

        if keys[pygame.K_UP]:
            self.acc.y = -PLAYER_ACC

        # Applying PLAYER_FRICTIONion
        self.acc.x += self.vel.x * PLAYER_FRICTION

        # Laws of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Boudary Conditions
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        if self.pos.y > HEIGHT:
            self.pos.y = 0

        self.rect.midbottom = self.pos


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(brown)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
