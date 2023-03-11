import pygame
from Assets.Scripts.UI.Components import Text, Font
from Assets.Scripts.Scenes.MainMenu import MainMenu

class Window:
    screen_width = 1600
    screen_height = 900
    screen = pygame.display.set_mode((screen_width, screen_height))

class Game:
    def Run():
        pygame.init()
        pygame.display.set_caption('Pong')
        Game.OpenWindow()

    def OpenWindow():
        BG_COLOR = (40, 40, 40)
        color_light = (200, 200, 200)
        color_dark = (80, 80, 80)
        color = (255,255,255)

        game_running = True
        gamePaused = False

        buttonText = Font.size['medium'].render('quit', True, color)
        # game loop
        while game_running:
            
            Window.screen.fill(BG_COLOR)

            menu = MainMenu()
            
            mouse = pygame.mouse.get_pos()

            # event handler
            for event in pygame.event.get():    

                if gamePaused and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    gamePaused = False     
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    gamePaused = True
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    Game.Quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Window.screen_width/2 <= mouse[0] <= Window.screen_width/2+140 and Window.screen_height/2 <= mouse[1] <= Window.screen_height/2+40:
                        pygame.quit()

                if event.type == pygame.QUIT:
                    game_running = False


            if Window.screen_width/2 <= mouse[0] <= Window.screen_width/2+140 and Window.screen_height/2 <= mouse[1] <= Window.screen_height/2+40:
                pygame.draw.rect(Window.screen, color_light,[Window.screen_width/2,Window.screen_height/2,140,40])    
            else:
                pygame.draw.rect(Window.screen, color_dark,[Window.screen_width/2,Window.screen_height/2,140,40])

            if gamePaused:
                Text.draw("Game is Paused", Font.size["big"], Font.color["white"], 200, 450)
            else:
                pass

            Window.screen.blit(buttonText , (Window.screen_width/2 + 25, Window.screen_height/2))

            pygame.display.update()

    def Quit():
        pygame.quit()
