import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scorpion Cursor Game")

# Load scorpion image (Make sure you have 'scorpion.png' in your working directory)
scorpion_img = pygame.image.load("scorpion.png")
scorpion_img = pygame.transform.scale(scorpion_img, (50, 50))  # Resize

# Hide system cursor
pygame.mouse.set_visible(False)

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen with black

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Draw the scorpion at the mouse position
    screen.blit(scorpion_img, (mouse_x - 25, mouse_y - 25))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
