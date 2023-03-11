from Assets.Scripts import Application

# run the game
def main():
   Application.Game.Run() 

# check if only one instance of the app (main function) is running
if __name__ == "__main__":
   main()