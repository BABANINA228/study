import pygame

import pygame_widgets
from pygame_widgets.button import Button

# Set up Pygame
pygame.init()
screen = pygame.display.set_mode((320, 320))
turn = 1
table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


class Table:
    __r = 0
    __c = 0

    def __init__(self):
        x = int(Table.__c * 110)
        y = int(Table.__r * 110)
        self.btn = Button(screen, x, y, 100, 100, onClick=lambda: set_figure(int(y / 110), int(x / 110)))
        if Table.__c <= 2:
            Table.__c += 1
        else:
            Table.__c = 0
            Table.__r += 1


def set_figure(r, c):
    global turn
    if turn == 1:
        table[r][c] = 1
        turn = 2
    elif turn == 2:
        table[r][c] = 2
        turn = 1
    pygame.draw.circle(screen, (111, 20, 222), (200, 100), 50, 10)
    print(table)


objs = [Table() for i in range(11)]

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    screen.fill((92, 92, 94))

    pygame_widgets.update(events)
    pygame.display.update()
