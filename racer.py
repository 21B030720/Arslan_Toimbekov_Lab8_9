from racer_classes import *

pygame.init()
#
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
background = pygame.image.load("Grass.png")
#
W = 1440
H = 900
Screen = pygame.display.set_mode( (W, H) )
pygame.display.set_caption("Racer")
done = False
FPS = pygame.time.Clock()
E1 = Enemy()
E2 = Enemy()
E3 = Enemy()
E4 = Enemy()
E5 = Enemy()
E6 = Enemy()
E7 = Enemy()
E8 = Enemy()
P = Player()
C = Coin()
player = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player.add(P)
coin = pygame.sprite.Group()
all_sprites.add(P, E1, E2, E3, E4, E5, E6, E7, E8)
enemies.add(E1, E2, E3, E4, E5, E6, E7, E8)
coin.add(C)
l = 1
while not done:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            done = False
            pygame.quit()
            sys.exit()
    Screen.fill(WHITE)
    Screen.blit(background, (0,0))
    for i in player:
        i.move(Screen)
    for i in enemies:
        i.move(Screen)
    if l == 1:
        C.draw(Screen)
        #l = 0
    if pygame.sprite.spritecollideany(C, player):
        for i in coin:
            i.move(Screen)


    Collision(Screen, all_sprites, P, enemies)
    pygame.display.flip()
    pygame.display.update()
    FPS.tick(60)
