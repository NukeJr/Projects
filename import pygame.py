import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 40
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Minecraft")

# Player starting position
player_pos = [COLS // 2, ROWS // 2]

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 1
    if keys[pygame.K_RIGHT] and player_pos[0] < COLS - 1:
        player_pos[0] += 1
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= 1
    if keys[pygame.K_DOWN] and player_pos[1] < ROWS - 1:
        player_pos[1] += 1

    # Drawing
    screen.fill(WHITE)  # Clear the screen

    # Draw the ground
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, GREEN, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    # Draw the player
    pygame.draw.rect(screen, BROWN, (player_pos[0] * GRID_SIZE, player_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()  # Update the screen
    pygame.time.delay(100)  # Control the frame rate