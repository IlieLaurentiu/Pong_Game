import pygame
from . import GameWindow

def Run():
    pygame.init()
    GameWindow.Open()

def Quit():
    pygame.quit()