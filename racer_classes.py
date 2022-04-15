import pygame
import random
import time
import sys
from pygame.locals import *
import datetime
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin1.png")
        self.image = pygame.transform.scale(self.image, (90, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (770, 300)
        self.count = 0
        #
        font_small = pygame.font.SysFont("Verdana", 200)
        self.scores = font_small.render(str(self.count), True, (0, 0, 0))
        #
    def move(self, Screen):
        self.count += 1
        #
        font_small = pygame.font.SysFont("Verdana", 200)
        self.scores = font_small.render(str(self.count), True, (0, 0, 0))
        #
        self.rect.center = (random.randint(100, 1340), random.randint(300, 800))
        self.draw(Screen)
    def draw(self, Screen):
        Screen.blit(self.image, self.rect)
        Screen.blit(self.scores, (1200, 20))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 1400), 0)

    def move(self, Screen):
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > 900):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 1410), 0)
            # time.sleep(random.randint(1, 3))
        self.draw(Screen)

    def draw(self, Screen):
        Screen.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (720, 450)

    def move(self, Screen):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            #if self.rect.top < 900:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            #if self.rect.bottom > 0:
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


"""k = datetime.datetime.now()
        k = k.second
        k = int(k)
        k %= 5
        m = random.randint(1, 5)"""