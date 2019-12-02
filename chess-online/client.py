import pygame
from network import Network
from player import Player


width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Client')

clientNumber = 0


def read_pos(str):
    print('str', str)
    str = str.split(",")
    print('str', str)
    print('int', int(str[0]), int(str[1]))
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + ',' + str(tup[1])


def redrawWindow(win, Player, Player2):
    win.fill((255, 255, 255))
    Player.draw(win)
    Player2.draw(win)

    pygame.display.update()


def main():
    run = True
    n = Network()
    startpos = read_pos(n.getPos())
    p = Player(startpos[0], startpos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (255, 255, 0))

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]

        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)


main()
