import pygame

#pygame setup
pygame.init()
SCREEN_WIDTH = 673
SCREEN_HEIGHT = 673
CHARACTER_SIZE = 80

#Character position variables
player_x = 375
player_y = 275

#Movement speed (pixels per frame)
player_speed = 5

pygame.display.set_caption("Yummy Chocolate Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load("background.jpg"),(SCREEN_WIDTH, SCREEN_HEIGHT))
character = pygame.transform.scale(pygame.image.load("images-removebg-preview.png"),(CHARACTER_SIZE, CHARACTER_SIZE) )
running = True

while running:
    #poll for events
    pygame.QUIT #event means the user clicked X to close your window
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
         player_x -= player_speed
    if keys[pygame.K_RIGHT]:
         player_x += player_speed
    if keys[pygame.K_UP]:
         player_y -= player_speed
    if keys[pygame.K_DOWN]:
         player_y += player_speed


    #Apply Boundary Restrictions (The Clamping)
    #Left boundary
    if player_x < 0:
         player_x = 0

    #Right boundary (Screen widt minus character width)
    if player_x > SCREEN_WIDTH - CHARACTER_SIZE:
         player_x = SCREEN_WIDTH - CHARACTER_SIZE

    #Top boundary
    if player_y < 0:
         player_y = 0

    #Bottom boundary (Screen height minus character height)
    if player_y > SCREEN_HEIGHT - CHARACTER_SIZE:
         player_y = SCREEN_HEIGHT - CHARACTER_SIZE

    #fill the screen with a color to wipe away anything from last frame
    screen.blit(background,(0,0))
    screen.blit(character, (player_x, player_y))



    #RENDER YOUR GAME HERE

    #flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)   #limits FPS to 60

pygame.quit()