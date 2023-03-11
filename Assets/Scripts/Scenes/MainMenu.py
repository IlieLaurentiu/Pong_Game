from Assets.Scripts.Scenes.Scene import Scene
from Assets.Scripts.UI.Components import *
#from Assets.Scripts.Application import Window

class MainMenu(Scene):
    def __init__(self):
        # Title
        Text.draw("Pong!", Font.size["big"], Font.color["white"], 750, 100)

        # To be replaced with buttons
        Text.draw("Play", Font.size["medium"], Font.color["white"], 150, 300)
        Text.draw("Shop", Font.size["medium"], Font.color["white"], 150, 400)
        Text.draw("Settings", Font.size["medium"], Font.color["white"], 150, 500)
        Text.draw("Quit", Font.size["medium"], Font.color["white"], 150, 600)
        
class Game(Scene):
    pass
