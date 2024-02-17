import pygame
pygame.init()


#*GLOBALS_____________________________________________________
global screen


#*PRE-SETUP____________________________________________________
#small variables for screen size
original_resolution = (320, 240)
aspect_ratio = original_resolution[0] / original_resolution[1]

#initialize the screen

screen = pygame.display.set_mode(original_resolution, pygame.RESIZABLE)


#*VARIABLES_____________________________________________________









#*FUNCTIONS_____________________________________________________











#*SETUP_________________________________________________________

pygame.display.set_caption("Prototype")
#? icon = pygame.image.load("assets/icon.png")
#? pygame.display.set_icon(icon)


#! _____________________________Main game loop__________________________________
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_F2:
                # we resize the window to 2x its size
                width, height = screen.get_size()
                screen = pygame.display.set_mode((width * 2, height * 2), pygame.RESIZABLE)
        

        
    keys = pygame.key.get_pressed()  # get the state of all keyboard keys
    if keys[pygame.K_RIGHT]:  
        print("Right arrow key is pressed")
        
    screen.fill((255, 255, 255))


    # *after* drawing everything, flip the display
    pygame.display.flip()
# !End of main game loop
pygame.quit()