import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

lvl2cloud_x = 250
lvl2cloud_y = 100
lvl2tree_x = 454
lvl2tree_y = 139
character_x = 70
character_y = 235

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
             print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    lvl2cloud_x -= 0.2
    if lvl2cloud_x + 70 == 0:
        lvl2cloud_x = WIDTH

    # DRAWING
    screen.fill((161, 220, 233))

    # GROUND
    pygame.draw.rect(screen, (0, 158, 96), (0, HEIGHT-160, WIDTH, 160))

    # CLOUDS
    # cloud_x = 250, cloud_y = 100
    pygame.draw.rect(screen, (245, 245, 245), (lvl2cloud_x, lvl2cloud_y, 70, 20))
    pygame.draw.rect(screen, (245, 245, 245), (lvl2cloud_x+10, lvl2cloud_y-15, 55, 15))
    
    # TREE
    # tree_x = 454, tree_y = 139
    # trunk
    pygame.draw.rect(screen, (106, 78, 56), (lvl2tree_x, lvl2tree_y, 55, 181))
    # leaves
    pygame.draw.rect(screen, (0, 101, 62), (lvl2tree_x-74, lvl2tree_y+19, 200, 40))
    pygame.draw.rect(screen, (0, 101, 62), (lvl2tree_x-54, lvl2tree_y-65, 180, 85))

    # CHARACTER
    # character_x = 70, character_y = 235
    # body
    pygame.draw.rect(screen, (0, 62, 101), (character_x+5, character_y+25, 35, 60))
    # head
    pygame.draw.rect(screen, (0, 62, 101), (character_x, character_y, 45, 40))
    pygame.draw.rect(screen, (224,172,105), (character_x+10, character_y+12, 25, 20))
    pygame.draw.rect(screen, (0, 101, 62), (character_x+15, character_y+20, 5, 5))
    pygame.draw.rect(screen, (0, 101, 62), (character_x+28, character_y+20, 5, 5))
    pygame.draw.rect(screen, (198,134,66), (character_x+15, character_y+28, 15, 2))

    
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
