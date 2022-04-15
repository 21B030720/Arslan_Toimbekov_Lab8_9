
from turtle import position
import pygame


def main():
    truth = True
    drawing_allow = False
    first_x = 0
    first_y = 0
    last_x = 0
    last_y = 0
    frame = 0
    r = 0
    pygame.init()
    screen = pygame.display.set_mode((1440, 900))
    clock = pygame.time.Clock()
    type = 1
    prevX = 0
    prevY = 0
    size = 20
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    BLUE = pygame.Color(0, 0, 255)
    GREEN = pygame.Color(0, 255, 0)
    RED = pygame.Color(255, 0, 0)
    color = WHITE
    screen.fill((0, 0, 0))

    isMouseDown = False

    while True:

        pressed = pygame.key.get_pressed()

        currentX = prevX
        currentY = prevY

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    type = 1
                if event.key == pygame.K_2:
                    type = 2
                if event.key == pygame.K_3:
                    type = 3
                if event.key == pygame.K_4:
                    type = 4
                if event.key == pygame.K_5:
                    type = 5
                if event.key == pygame.K_6:
                    type = 6
                if event.key == pygame.K_i:
                    size += 5
                if event.key == pygame.K_d:
                    size -= 5
                if event.key == pygame.K_b:
                    color = BLACK
                if event.key == pygame.K_l:
                    color = BLUE
                if event.key == pygame.K_g:
                    color = GREEN
                if event.key == pygame.K_r:
                    color = RED
                if event.key == pygame.K_m:
                    if r == 400:
                        r = 0
                    r += 1
                if event.key == pygame.K_n:
                    if r == -400:
                        r = 0
                    r -= 1
                if event.key == pygame.K_h:
                    frame += 1
                if event.key == pygame.K_f:
                    frame -= 1

            if type == 6 and event.type == pygame.MOUSEBUTTONDOWN and truth:
                truth = False
                drawing_allow = True
                first_x = event.pos[0]
                first_y = event.pos[1]
            if type == 6 and drawing_allow:
                last_x = event.pos[0]
                last_y = event.pos[1]
            if drawing_allow and type == 6 and event.type == pygame.MOUSEBUTTONUP:
                truth = True
                drawing_allow = False
                pygame.draw.polygon(surface=screen, color=color,
                                    points=[(first_x, first_y), (last_x, first_y),
                                            ((first_x+last_x)/2 ,last_y)], width=frame)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isMouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    isMouseDown = False

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                currentX =  event.pos[0]
                currentY =  event.pos[1]


        if isMouseDown:
            if type == 1:
                pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY))
            if type == 2:
                pygame.draw.rect(screen, color, pygame.Rect(prevX-10, prevY-10, size, size), frame)
            if type == 3:
                pygame.draw.circle(screen, color, (prevX, prevY), size, frame)
            if type == 4:
                pygame.draw.circle(screen, (0, 0, 0), (prevX, prevY), size, 0)
            if type == 5:
                if r % 4 == 0:
                    pygame.draw.polygon(surface=screen, color=color,
                                        points=[(prevX - (10+size), prevY + (10+size)), (prevX, prevY - (10+size)),
                                                (prevX + (10+size), prevY + (10+size))], width = frame)

                elif r % 4 == 1:
                    pygame.draw.polygon(surface=screen, color=color,
                                        points=[(prevX - (10+size), prevY + (10+size)), (prevX - (10+size), prevY - (10+size)),
                                                (prevX + (10+size), prevY)], width = frame)
                elif r % 4 == 2:
                    pygame.draw.polygon(surface=screen, color=color,
                                        points=[(prevX - (10+size), prevY - (10+size)), (prevX, prevY + (10+size)),
                                                (prevX + (10+size), prevY - (10+size))], width = frame)
                elif r % 4 == 3:
                    pygame.draw.polygon(surface=screen, color=color,
                                        points=[(prevX - (10+size), prevY), (prevX + (10+size), prevY - (10+size)),
                                                (prevX + (10+size), prevY + (10+size))], width = frame)


        prevX = currentX
        prevY = currentY

        pygame.display.flip()
        clock.tick(60)

main()