import pygame

pygame.font.init()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((1000, 1000))

FONT_SIZE = 30
font = pygame.font.SysFont("arialblack", FONT_SIZE)
TEXT_COLOR = (255, 255, 255)

# Use this function to add text into the game, using text, font, 
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    textRect = img.get_rect()
    textRect.center = (x // 2, y // 2)
    screen.blit(img, (x, y))
