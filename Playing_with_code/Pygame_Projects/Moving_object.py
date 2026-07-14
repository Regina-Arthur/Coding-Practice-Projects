import pygame  # Import the pygame library for game development

# --- Pygame Initialization and Setup ---
pygame.init()  # Initialize all imported pygame modules

# Screen dimensions
SCREEN_WIDTH = 673   # Width of the game window in pixels
SCREEN_HEIGHT = 673  # Height of the game window in pixels

# Player character size
CHARACTER_SIZE = 80  # Width and height of the player sprite in pixels

# --- Player Position Variables ---
player_x = 375  # Initial X position of the player (center-ish)
player_y = 275  # Initial Y position of the player

# Movement speed configuration
player_speed = 5  # How many pixels the player moves per frame

# --- Window and Asset Loading ---
pygame.display.set_caption("Yummy Chocolate Game")  # Set the title of the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create the game window surface
clock = pygame.time.Clock()  # Create a Clock object to control the frame rate

# Load and scale background image to fit screen
background = pygame.transform.scale(
    pygame.image.load("background.jpg"), 
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# Load and scale player character image
character = pygame.transform.scale(
    pygame.image.load("images-removebg-preview.png"), 
    (CHARACTER_SIZE, CHARACTER_SIZE)
)

# Main game loop control variable
running = True

# --- Main Game Loop ---
while running:
    # --- Event Polling ---
    for event in pygame.event.get():  # Iterate over all events in the queue
        if event.type == pygame.QUIT:  # Check if the user clicked the close button (X)
            running = False  # Stop the game loop to close the window

    # --- Input Handling (Movement) ---
    keys = pygame.key.get_pressed()  # Get the current state of all keyboard keys

    # Move player LEFT
    if keys[pygame.K_LEFT]:
        player_x -= player_speed  # Decrease X position

    # Move player RIGHT
    if keys[pygame.K_RIGHT]:
        player_x += player_speed  # Increase X position

    # Move player UP
    if keys[pygame.K_UP]:
        player_y -= player_speed  # Decrease Y position (screen coordinates go down)

    # Move player DOWN
    if keys[pygame.K_DOWN]:
        player_y += player_speed  # Increase Y position

    # --- Boundary Checks (Clamping) ---
    # Prevent player from going off the left edge
    if player_x < 0:
        player_x = 0

    # Prevent player from going off the right edge (screen width minus character width)
    if player_x > SCREEN_WIDTH - CHARACTER_SIZE:
        player_x = SCREEN_WIDTH - CHARACTER_SIZE

    # Prevent player from going off the top edge
    if player_y < 0:
        player_y = 0

    # Prevent player from going off the bottom edge (screen height minus character height)
    if player_y > SCREEN_HEIGHT - CHARACTER_SIZE:
        player_y = SCREEN_HEIGHT - CHARACTER_SIZE

    # --- Drawing / Rendering ---
    screen.blit(background, (0, 0))  # Draw the background image at the top-left corner (0,0)
    screen.blit(character, (player_x, player_y))  # Draw the player character at current position

    # --- Display Update ---
    pygame.display.flip()  # Update the entire display surface to show the new frame

    # --- Frame Rate Control ---
    clock.tick(60)  # Limit the game to 60 frames per second (FPS)

# --- Cleanup ---
pygame.quit()  # Uninitialize all pygame modules and exit cleanly