import pygame

from Board import UI_Board
from setting import Setting



if __name__ == '__main__':
    (width, height) = (700, 700)
    screen = pygame.display.set_mode((width, height))
    
    board = UI_Board(screen)
    setting = Setting(screen)
    pygame.display.flip()
    runing = True

    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False