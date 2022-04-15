from random import choice
import random
import os
import pygame
from pygame.locals import *
#from snake_classes import FF, Snake
#os.chdir('Assets')
pygame.init()
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x, self.y = x, y
        self.image = pygame.image.load("snake_wall.png")
        self.image = pygame.transform.scale(self.image, (90, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    def move(self, Screen):
        self.draw(Screen)
    def draw(self, Screen):
        Screen.blit(self.image, self.rect)
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.body = []
        self.image = pygame.transform.scale(pygame.image.load('snake_head.png'), (30, 30))
        self.apple = pygame.transform.scale(pygame.image.load('snake_apple.png'), (30, 30))
        self.im_of_body = pygame.transform.scale(pygame.image.load('snake_body.png'), (30, 30))
        self.rect = self.image.get_rect(center=(WIDTH / 2 - 7.5, 10 + HEIGHT / 2 - 7.5))
        self.direction = (15, 0)
        self.apple_rect = self.apple.get_rect(center=(choice(sequence), 20 + choice(sequence)))

    def move(self, screen):
        for i in range(len(self.body) - 1):
            self.body[i] = self.body[i + 1]
            screen.blit(self.im_of_body, self.im_of_body.get_rect(center=self.body[i]))
        if self.body:
            self.body[-1] = (self.rect.center)
            screen.blit(self.im_of_body, self.im_of_body.get_rect(center=self.body[-1]))
        self.rect.move_ip(self.direction)
        screen.blit(pygame.transform.rotate(self.image, ({1: 0, 0: 0, -1: 1}[self.direction[1] / 15]) * (180) + (
                    self.direction[0] / 15) * 90), self.rect)

    def spawn_apple(self, screen):
        while self.apple_rect.center in self.body or self.apple_rect.center == self.rect.center:
            self.apple_rect = self.apple.get_rect(center=(choice(sequence), 20 + choice(sequence)))
        screen.blit(self.apple, self.apple_rect)

    def eat_apple(self, screen):
        self.body.append((-20, -20))
        self.spawn_apple(screen)

font = pygame.font.SysFont('comicans', 30,True, False)
font_large = pygame.font.SysFont('comicans', 100, True, False)
BACKGROUND = pygame.transform.scale(pygame.image.load('Grass.png'), (720,720))
pygame.init()
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
Score = 0
m = 0
size = WIDTH, HEIGHT = (720,740)
speed = 25

sequence = [7.5 + 15*i for i in range(1,48)]

        
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

W11 = Wall(120, 70)
W22 = Wall(190, 70)
W33 = Wall(300, 70)
W1 = Wall(440, 70)
W2 = Wall(290, 70)
W3 = Wall(380, 70)
W4 = Wall(440, 500)
W5 = Wall(120, 200)
W6 = Wall(450, 120)
W7 = Wall(400, 300)
W8 = Wall(350, 230)

k = [W1, W2, W3, W4, W5, W6, W7]
S = Snake()
walls = pygame.sprite.Group()
player = pygame.sprite.Group()
walls.add(W11, W22, W33)
player.add(S)
def main():
    running = True
    screen = pygame.display.set_mode(size)
    screen.fill((255,255,255))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if  event.key == K_UP and S.direction != (0,15) and event.key != K_DOWN:
                    S.direction = (0,-15)
                if event.key == K_DOWN and S.direction != (0,-15) and event.key != K_UP:
                    S.direction = (0,15)
                if event.key==K_RIGHT and S.direction != (-15,0) and event.key!=K_LEFT:
                    S.direction = (15,0)
                if event.key==K_LEFT and S.direction != (15,0) and event.key!=K_RIGHT:
                    S.direction = (-15,0)    

        screen.blit(BACKGROUND, (0,20))
        pygame.draw.rect(screen, pygame.Color('lime'),(0,0,WIDTH,20))
        S.spawn_apple(screen)
        for i in walls:
            i.draw(screen)
        S.move(screen)
        if S.rect.center == S.apple_rect.center:
            global Score
            global m
            m = Score // 5
            S.eat_apple(screen)
            for i in walls:
                i.move(screen)
            Score+=1
            if m != Score // 5 and m < len(k):
                walls.add(k[m])
        screen.blit(font.render(f'Score:{Score}         Level:{Score//5}',True, WHITE),(0,0))
        speed = 10 + (Score//5)*2
        if S.rect.x < 2.5 or S.rect.x+17.5 > WIDTH or S.rect.y < 10 or S.rect.y+17.5 > HEIGHT or S.rect.center in S.body or pygame.sprite.spritecollideany(S, walls):
            pygame.mixer.music.stop()
            screen.fill((111,111,111))
            screen.blit(font_large.render(f'GAME OVER!',True,WHITE),(100,100))
            screen.blit(font.render(f'Yor score: {Score}',True,WHITE),(250,180))
            screen.blit(font.render(f'Level:{Score//5}',True,WHITE),(270,210))
            pygame.display.update()
            pygame.time.delay(3000)
            running = False
        clock.tick(speed)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()


