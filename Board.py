import pygame

class UI_Board():
    def __init__(self, screen) -> None:
        self.screen = screen
        # Screen setting
        background_color = (255,255,255)
        line_color = (0, 0, 0)
        dist = 500 / 9

        self.background_set(background_color)
        self.create_line(line_color, dist)

    def background_set(self, background_color):
        # Screen setting
        pygame.display.set_caption("Sudoku")
        self.screen.fill(background_color)
    
    def create_line(self, line_color, dist):
        # Draw line
        for i in range(10):
            if(i % 3 == 0):
                thick = 7
            else:
                thick = 1

            if(i == 0):
                pygame.draw.line(self.screen, line_color, (0, 3), (500, 3), thick) # Row
                pygame.draw.line(self.screen, line_color, (3, 0), (3, 500), thick) # col
            elif(i == 9):
                pygame.draw.line(self.screen, line_color, (0, 500), (503, 500), thick) # Row
                pygame.draw.line(self.screen, line_color, (500, 0), (500, 503), thick) # col
            else:
                pygame.draw.line(self.screen, line_color, (0, i * dist), (500, i * dist), thick) # Row
                pygame.draw.line(self.screen, line_color, (i * dist, 0), (i * dist, 500), thick) # col
    
    def fillBoard(self, board):
        pass