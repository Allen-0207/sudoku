import pygame

font = pygame.font.SysFont('Arial', 40)

class Button():
    def __init__(self, x, y, width, height, buttonText="Button", onClickFunction=None) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onClickFunction

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))


class Setting():
    def __init__(self, screen) -> None:
        self.screen = screen
        self.easy = Button()
