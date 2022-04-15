from r_classes import *

pygame.init()

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
background = pygame.image.load("AnimatedStreet.png")

W = 400
H = 600
Screen = pygame.display.set_mode( (W, H) )
pygame.display.set_caption("Racer")
done = False
FPS = pygame.time.Clock()
E1 = Enemy()

P = Player()
C = Coin()
C2 = Coin2()

player = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player.add(P)
coin = pygame.sprite.Group()
coin2 = pygame.sprite.Group()
all_sprites.add(P, E1)
enemies.add(E1)
coin.add(C)
coin2.add(C2)

score = 0
#speedik = 10
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
    if 1 == 1:
        C.draw(Screen)
    global count
    if score % 5 == 0:
        #speedik += 2
        #print(score)
        C2.draw(Screen)

    if pygame.sprite.spritecollideany(C, player):
        score += 1
        for i in coin:
            i.move(Screen)
    if pygame.sprite.spritecollideany(C2, player):
        score += 1
        for i in coin2:
            i.move(Screen)

    Collision(Screen, all_sprites, P, enemies)
    pygame.display.flip()
    pygame.display.update()
    FPS.tick(60)
