import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Tunnel Effect")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Tunnel parameters
num_circles = 20
max_radius = 400
min_radius = 50
depth = 5

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Calculate time-based offset
    offset = pygame.time.get_ticks() / 1000

    # Draw the tunnel
    for i in range(num_circles):
        t = i / num_circles
        radius = max_radius * (1 - t) + min_radius * t
        x = width // 2 + math.cos(t * depth + offset) * radius / 4
        y = height // 2 + math.sin(t * depth + offset) * radius / 4
        color = [int(255 * (1 - t))] * 3
        pygame.draw.circle(screen, color, (int(x), int(y)), int(radius), 1)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
