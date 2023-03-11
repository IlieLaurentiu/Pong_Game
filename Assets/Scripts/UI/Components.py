import pygame
from Assets.Scripts import Application

pygame.font.init()

# Use this class to manipulate text properties
class Font:
    size = {
        "big" : pygame.font.SysFont("arialblack", 32),
        "medium" : pygame.font.SysFont("arialblack", 24),
        "small" : pygame.font.SysFont("arialblack", 16)
    }

    color = {
        "white" : (255, 255, 255),
        "black" : (0, 0, 0)
    }

# Use this class's method to add text into the game by drawing it on screen
class Text:
    def draw(text, font, text_color, x, y):
        img = font.render(text, True, text_color)
        Application.Window.screen.blit(img, (x, y))

# Use this class for UI buttons
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self, surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False