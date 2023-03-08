import pygame
from Assets.Scripts import Application

pygame.font.init()

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

class Text:

    # Use this function to add text into the game, using text, font, color and coordinates
    def draw_text(text, font, text_color, x, y):
        img = font.render(text, True, text_color)
        Application.Window.screen.blit(img, (x, y))

class Button:
    pass