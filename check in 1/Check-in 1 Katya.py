import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

tree_x = 454
tree_y = 139

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

    # DRAWING
    screen.fill((161, 220, 233))

    # GROUND
    pygame.draw.rect(screen, (0, 158, 96), (0, HEIGHT-160, WIDTH, 160))
    # TREE
    # tree_x = 454, tree_y = 139
    pygame.draw.rect(screen, (106, 78, 56), (tree_x, tree_y, 55, 181))
    pygame.draw.rect(screen, (0, 101, 62), (tree_x-74, tree_y+19, 200, 40))
    pygame.draw.rect(screen, (0, 101, 62), (tree_x-54, tree_y-65, 180, 85))

    # CHARACTER
    character_x = 70
    character_y = 235
    pygame.draw.rect(screen, (0, 62, 101), (character_x, character_y, 45, 40))
    pygame.draw.rect(screen, (0, 62, 101), (character_x+10, character_y+25, 25, 60))
    # Still working on it

    
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
