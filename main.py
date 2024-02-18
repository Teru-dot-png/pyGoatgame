import pygame
pygame.init()


#*GLOBALS_____________________________________________________
global screen

#*PRE-SETUP____________________________________________________
#small variables for screen size
original_resolution = (800, 600)
aspect_ratio = original_resolution[0] / original_resolution[1]

#initialize the screen

screen = pygame.display.set_mode(original_resolution, pygame.RESIZABLE)

clock = pygame.time.Clock()

pygame.mixer.init()
#*VARIABLES_____________________________________________________

bad_explosion = pygame.mixer.Sound('Sounds/Bad_explosion.mp3')
bad_explosion.set_volume(0.1)

sound_played1 = False
sound_played2 = False

screencount = 0

P1 = {
    'name': 'Amie',
    'x': 133,
    'y': 270,
    'speed': 5,
    'image': pygame.image.load('characters/amisita.png'),
    'image2': pygame.image.load('characters/amisitalewd.png'),
    'alt': False,
    'last_direction': 'right',
    'directions': {
        'up': pygame.K_w,
        'down': pygame.K_s,
        'left': pygame.K_a,
        'right': pygame.K_d,
    },
    'can_move': True
}

P2 = {
    'name': 'Felix',
    'x': 600,
    'y': 270,
    'speed': 5,
    'image': pygame.image.load('characters/Felixito.png'),
    'image2': pygame.image.load('characters/Felixitoblush.png'),
    'alt': False,
    'last_direction': 'left',
    'directions': {
        'up': pygame.K_UP,
        'down': pygame.K_DOWN,
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT,
    },
    'can_move': True
}

P3 = {
    'name': 'placeholder',
    'x': 400,
    'y': 300,
    'speed': 5,
    'image': pygame.image.load('characters/Felixito.png'),
    'image2': pygame.image.load('characters/Felixitoblush.png'),
    'last_direction': 'left',
    'directions': {
        'up': pygame.K_i,
        'down': pygame.K_k,
        'left': pygame.K_j,
        'right': pygame.K_l,
    },
    'can_move': True
}

circleX1, circleY1 = original_resolution[0] / 2, original_resolution[1] / 2
circleX2, circleY2 = original_resolution[0] / 2, original_resolution[1] / 2

speed = 3

#*FUNCTIONS_____________________________________________________

# @params: directions: dictionary of directions and their respective keys
# @params: keys: the current state of all keyboard keys
# @params: circleX: the x position of the circle
# @params: circleY: the y position of the circle
# @params: speed: the speed at which the circle moves
# @returns: the new x and y position of the circle
def handle_movement(player, keys):
    if not player['can_move']:
        return
    for direction, key in player['directions'].items():
        if keys[key]:
            print(f"{direction} arrow key is pressed")
            if direction == 'right':
                player['x'] += player['speed']
                if player['last_direction'] != 'right':
                    player['image'] = pygame.transform.flip(player['image'], True, False)
                    player['image2'] = pygame.transform.flip(player['image2'], True, False)
                    player['last_direction'] = 'right'
            elif direction == 'left':
                player['x'] -= player['speed']
                if player['last_direction'] != 'left':
                    player['image'] = pygame.transform.flip(player['image'], True, False)
                    player['image2'] = pygame.transform.flip(player['image2'], True, False)
                    player['last_direction'] = 'left'
            elif direction == 'up':
                player['y'] -= player['speed']
            elif direction == 'down':
                player['y'] += player['speed']

#render handler
def render_handler():
    screen.fill((255, 255, 255))
    if P1['alt']:
        screen.blit(P1['image2'], (P1['x'], P1['y']))
    else:
        screen.blit(P1['image'], (P1['x'], P1['y']))

    if P2['alt']:
        screen.blit(P2['image2'], (P2['x'], P2['y']))
    else:
        screen.blit(P2['image'], (P2['x'], P2['y']))
    #screen.blit(P3['image'], (P3['x'], P3['y']))   
    pass







#*SETUP_________________________________________________________

pygame.display.set_caption("Prototype") #? Set the title of the window
#? icon = pygame.image.load("assets/icon.png") #? Load the icon
#? pygame.display.set_icon(icon) #? Set the icon


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
                if screencount < 2:
                    width, height = screen.get_size()
                    screen = pygame.display.set_mode((width * 1.5, height * 1.5), pygame.RESIZABLE)
                    screencount += 1
                else:
                    screencount = 0
                    screen = pygame.display.set_mode(original_resolution, pygame.RESIZABLE)
            elif event.key == pygame.K_SPACE:
                # toggle bool value alt from P1 between True and False
                if P1['alt']:
                    P1['alt'] = False
                else:
                    P1['alt'] = True

                

        

        
    keys = pygame.key.get_pressed()  # get the state of all keyboard keys
    

    handle_movement(P1, keys)
    handle_movement(P2, keys)
    #handle_movement(P3, keys)

    
        

    P1hitbox = pygame.Rect(P1['x'], P1['y'], P1['image'].get_width() - 50, P1['image'].get_height())
    P1ALTbox = pygame.Rect(P1['x'], P1['y'], P1['image'].get_width() + 100, P1['image'].get_height() + 31)  
    P2ALTbox = pygame.Rect(P2['x'], P2['y'], P2['image'].get_width() + 100, P2['image'].get_height() + 31)
    P2hitbox = pygame.Rect(P2['x'], P2['y'], P2['image'].get_width() - 50, P2['image'].get_height())
    #P3hitbox = pygame.Rect(P3['x'], P3['y'], P3['image'].get_width(), P3['image'].get_height())

    #if alt is true we make a colision check p1 with p2 alt hitbox
    if P1['alt']:
        if P1ALTbox.colliderect(P2ALTbox):
            print("alt colided with alt")
            P2['alt'] = True
    else:
        P2['alt'] = False
    
    # we are gonna see if the circle collides with the hitbox of P2
    


    if P1hitbox.colliderect(P2hitbox):
        print("Collision detected!")
    
    #if P3hitbox.colliderect(P1hitbox) and not sound_played1:
    #    print("Felixito has murdered P1!")
    #    P1['can_move'] = False
    #    bad_explosion.play()
    #    sound_played1 = True#

    #if P3hitbox.colliderect(P2hitbox) and not sound_played2:
    #    print("Felixito has murdered P2!")
    #    P2['can_move'] = False
    #    bad_explosion.play()
    #    sound_played2 = True


    render_handler()

    # *after* drawing everything, flip the display
    clock.tick(60)
    pygame.display.flip()
    
# !End of main game loop
pygame.quit()