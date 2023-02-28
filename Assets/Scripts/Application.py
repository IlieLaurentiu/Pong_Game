import pygame
from Assets.Scripts.UI.Menu import * 


def Run():
    pygame.init()
    pygame.display.set_caption('Pong')
    OpenWindow()

def OpenWindow():

    BG_COLOR = (40, 40, 40)
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 900
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    gameRunning = True
    # event handler
    while gameRunning:
        for event in pygame.event.get():    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Space pressed")
                
            if event.type == pygame.QUIT:
                gameRunning = False

            screen.fill(BG_COLOR)
            draw_text("Press SPACE to write to console", font, TEXT_COLOR, 200, 450)

            pygame.display.flip()
            pygame.display.update()
        

def Quit():
    pygame.quit()