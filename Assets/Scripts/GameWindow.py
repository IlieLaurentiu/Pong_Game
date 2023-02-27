import pygame

def Open():
    # Define the background colour using RGB color coding.
    background_colour = (25, 25, 25)
    # Define the dimensions of
    # screen object(width,height)
    screen = pygame.display.set_mode((1600, 900))
            
    # Set the caption of the screen
    pygame.display.set_caption('Pong')
            
    # Fill the background colour to the screen
    screen.fill(background_colour)
            
    # Update the display using flip
    pygame.display.flip()
            
    # Variable to keep our game loop running
    running = True
            
    # game loop
    while running:
        # for loop through the event queue  
        for event in pygame.event.get():
            # Check for QUIT event      
            if event.type == pygame.QUIT:
                running = False
