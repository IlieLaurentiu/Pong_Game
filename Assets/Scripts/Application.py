import pygame
from Assets.Scripts.UI.Components import Text, Font
from Assets.Scripts.Scenes.MainMenu import MainMenu
# from Assets.Scenes.MainMenu import *

class Window:
    screen_width = 1600
    secreen_height = 900
    screen = pygame.display.set_mode((screen_width, secreen_height))

class Game:
    def Run():
        pygame.init()
        pygame.display.set_caption('Pong')
        Game.OpenWindow()

    def OpenWindow():

        BG_COLOR = (40, 40, 40)

        gameRunning = True
        gamePaused = False

        # game loop
        while gameRunning:
            
            Window.screen.fill(BG_COLOR)

            menu = MainMenu()
            
            # event handler
            for event in pygame.event.get():    

                if gamePaused and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    gamePaused = False     
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    gamePaused = True
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    Game.Quit()

                if event.type == pygame.QUIT:
                    gameRunning = False


            if gamePaused:
                Text.draw_text("Game is Paused", Font.size["big"], Font.color["white"], 200, 450)
            else:
                pass

            pygame.display.flip()
            pygame.display.update()

    def Quit():
        pygame.quit()
