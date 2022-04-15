import pygame
import random
import time
import sys
from pygame.locals import *
count = 0
speedik = 10
class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Bitcoin.png")
        self.image = pygame.transform.scale(self.image, (90, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 300)
        self.count = 0

        font_small = pygame.font.SysFont("Verdana", 70)
        self.scores = font_small.render(str(count), True, (0, 0, 0))

    def move(self, Screen):
        global count
        count += 3

        font_small = pygame.font.SysFont("Verdana", 70)
        self.scores = font_small.render(str(count), True, (0, 0, 0))

        self.rect.center = (random.randint(70, 330), random.randint(200, 530))
        self.draw(Screen)

    def draw(self, Screen):
        global count
        font_small = pygame.font.SysFont("Verdana", 70)
        self.scores = font_small.render(str(count), True, (0, 0, 0))
        Screen.blit(self.image, self.rect)
        Screen.blit(self.scores, (10, 10))


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin1.png")
        self.image = pygame.transform.scale(self.image, (90, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 300)
        self.count = 0

        font_small = pygame.font.SysFont("Verdana", 70)
        self.scores = font_small.render(str(self.count), True, (0, 0, 0))

    def move(self, Screen):
        global count
        count += 1

        font_small = pygame.font.SysFont("Verdana", 70)
        self.scores = font_small.render(str(count), True, (0, 0, 0))

        self.rect.center = (random.randint(70, 330), random.randint(200, 530))
        self.draw(Screen)

    def draw(self, Screen):
        global count
        font_small = pygame.font.SysFont("Verdana", 70)
        self.scores = font_small.render(str(count), True, (0, 0, 0))
        Screen.blit(self.image, self.rect)
        Screen.blit(self.scores, (10, 10))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 300), 0)

    def move(self, Screen):
        global count
        global speedik
        if speedik < count / 10:
            speedik = count / 10
        print(speedik)
        self.rect.move_ip(0, speedik)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            # time.sleep(random.randint(1, 3))
        self.draw(Screen)

    def draw(self, Screen):
        Screen.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self, Screen):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
        if pressed_keys[K_LEFT]:
            if self.rect.left > 0:
                self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT]:
            if self.rect.right < 1440:
                self.rect.move_ip(10, 0)
        self.draw(Screen)

    def draw(self, Screen):
        Screen.blit(self.image, self.rect)


def Collision(Screen, all_sprites, P, enemies):
    if pygame.sprite.spritecollideany(P, enemies):
        Screen.fill((200, 200, 200))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(1)
        pygame.quit()
        sys.exit()
