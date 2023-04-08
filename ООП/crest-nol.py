import pygame
import pygame_widgets
from pygame_widgets.button import Button

# Set up Pygame
pygame.init()
screen = pygame.display.set_mode((320, 320))

table = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)


class Table:
    __r = 0
    __c = 0
    turn = 'a'
    btn_srf = pygame.Surface((100, 100))

    def __init__(self):
        self.alraedy_clicked = False
        x = int(Table.__c * 110)
        y = int(Table.__r * 110)
        self.btn = Button(Table.btn_srf, x, y, 100, 100, onClick=lambda: self.set_figure(int(y / 110), int(x / 110)))
        screen.blit(Table.btn_srf, (x, y))
        if Table.__c <= 2:
            Table.__c += 1
        else:
            Table.__c = 0
            Table.__r += 1

    def set_figure(self, r, c):
        if self.alraedy_clicked:
            pass
        else:
            if Table.turn == 'a':
                table[r][c] = 'a'
                Table.turn = 'b'
                pygame.draw.line(screen, (223, 25, 86),
                                 [c * 110 + 5, r * 110 + 5],
                                 [c * 110 + 95, r * 110 + 95], 10)
                pygame.draw.line(screen, (223, 25, 86),
                                 [c * 110 + 95, r * 110 + 5],
                                 [c * 110 + 5, r * 110 + 95], 10)
            elif Table.turn == 'b':
                table[r][c] = 'b'
                Table.turn = 'a'
                pygame.draw.circle(screen, (46, 99, 221),
                                   (c * 110 + 50, r * 110 + 50), 45, 8)
            self.alraedy_clicked = True
            pygame.display.update()

    @staticmethod
    def is_win():
        global run
        if ''.join(table[0]) == 'aaa' or ''.join(table[1]) == 'aaa' or ''.join(table[2]) == 'aaa':
            print('Крестики победили')
            run = False
        if (table[0][0] == 'a' and table[1][0] == 'a' and table[2][0] == 'a') or (
                table[0][1] == 'a' and table[1][1] == 'a' and table[2][1] == 'a') or (
                table[0][2] == 'a' and table[1][2] == 'a' and table[2][2] == 'a'):
            print('Крестики победили')
            run = False
        if (table[0][0] == 'a' and table[1][1] == 'a' and table[2][2] == 'a') or (
                table[0][2] == 'a' and table[1][1] == 'a' and table[2][0] == 'a'):
            print('Крестики победили')
            run = False

        if ''.join(table[0]) == 'bbb' or ''.join(table[1]) == 'bbb' or ''.join(table[2]) == 'bbb':
            print('Нолики победили')
            run = False
        if (table[0][0] == 'b' and table[1][0] == 'b' and table[2][0] == 'b') or (
                table[0][1] == 'b' and table[1][1] == 'b' and table[2][1] == 'b') or (
                table[0][2] == 'b' and table[1][2] == 'b' and table[2][2] == 'b'):
            print('Нолики победили')
            run = False
        if (table[0][0] == 'b' and table[1][1] == 'b' and table[2][2] == 'b') or (
                table[0][2] == 'b' and table[1][1] == 'b' and table[2][0] == 'b'):
            print('Нолики победили')
            run = False


screen.fill((92, 92, 94))
objs = [Table() for i in range(11)]

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    Table.is_win()
    pygame_widgets.update(events)
    pygame.display.update()
