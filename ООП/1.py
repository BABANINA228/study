import pygame

pygame.init()

size = [500,500]
speed = [2,2]
screen = pygame.display.set_mode(size)


table = pygame.image.load('table.jpg')
table_rect = table.get_rect()



paddle_one = table = pygame.image.load('paddle.jpg')
paddle_one_rect = paddle_one.get_rect()





while True:

    screen.blit(table, table_rect)

    screen.blit(paddle_one, paddle_one_rect)
    pygame.display.update()