import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Random Dice Game")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 200, 100)
BUTTON_HOVER_COLOR = (150, 250, 150)
DICE_COLOR = (200, 200, 200)
DOT_COLOR = BLACK

# Function to draw a dice face
def draw_dice(surface, value, rect):
    pygame.draw.rect(surface, DICE_COLOR, rect, border_radius=30)
    
    # Calculate dot positions
    dots = {
        1: [(rect.centerx, rect.centery)],
        2: [(rect.left + rect.width * 0.25, rect.top + rect.height * 0.25),
            (rect.right - rect.width * 0.25, rect.bottom - rect.height * 0.25)],
        3: [(rect.left + rect.width * 0.25, rect.top + rect.height * 0.25),
            (rect.centerx, rect.centery),
            (rect.right - rect.width * 0.25, rect.bottom - rect.height * 0.25)],
        4: [(rect.left + rect.width * 0.25, rect.top + rect.height * 0.25),
            (rect.right - rect.width * 0.25, rect.top + rect.height * 0.25),
            (rect.left + rect.width * 0.25, rect.bottom - rect.height * 0.25),
            (rect.right - rect.width * 0.25, rect.bottom - rect.height * 0.25)],
        5: [(rect.left + rect.width * 0.25, rect.top + rect.height * 0.25),
            (rect.right - rect.width * 0.25, rect.top + rect.height * 0.25),
            (rect.centerx, rect.centery),
            (rect.left + rect.width * 0.25, rect.bottom - rect.height * 0.25),
            (rect.right - rect.width * 0.25, rect.bottom - rect.height * 0.25)],
        6: [(rect.left + rect.width * 0.25, rect.top + rect.height * 0.25),
            (rect.left + rect.width * 0.25, rect.centery),
            (rect.left + rect.width * 0.25, rect.bottom - rect.height * 0.25),
            (rect.right - rect.width * 0.25, rect.top + rect.height * 0.25),
            (rect.right - rect.width * 0.25, rect.centery),
            (rect.right - rect.width * 0.25, rect.bottom - rect.height * 0.25)]
    }
    
    for dot in dots[value]:
        pygame.draw.circle(surface, DOT_COLOR, (int(dot[0]), int(dot[1])), 15)

# Initial dice roll
current_dice = random.randint(1, 6)

# Font setup
font = pygame.font.Font(None, 48)

# Dice button
button_width, button_height = 200, 80  # Increased button size
button_rect = pygame.Rect((screen.get_width() - button_width) // 2, screen.get_height() - button_height - 20, button_width, button_height)

# Dice rectangle
dice_size = 150
dice_rect = pygame.Rect((screen.get_width() - dice_size) // 2, (screen.get_height() - dice_size) // 2, dice_size, dice_size)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Animation effect for rolling dice
                for _ in range(10):
                    current_dice = random.randint(1, 6)
                    pygame.time.wait(100)  # Small delay for animation effect
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Roll the dice on space bar press
            current_dice = random.randint(1, 6)

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the dice
    draw_dice(screen, current_dice, dice_rect)

    # Draw the button
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_rect)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    
    # Draw button text
    text = font.render('Roll Dice', True, BLACK)
    screen.blit(text, (button_rect.x + (button_width - text.get_width()) // 2, button_rect.y + (button_height - text.get_height()) // 2))
    
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
