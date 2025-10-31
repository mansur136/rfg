import pygame
import sys
import os
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock Meme")

BASE_DIR = os.path.join(os.path.dirname(__file__), "images")

background = pygame.image.load(os.path.join(BASE_DIR, "background.png")).convert_alpha()
right_hand = pygame.image.load(os.path.join(BASE_DIR, "right_hand.png")).convert_alpha()
left_hand = pygame.image.load(os.path.join(BASE_DIR, "left_hand.png")).convert_alpha()

scale_factor = 0.33
right_hand = pygame.transform.rotozoom(right_hand, 0, scale_factor)
left_hand = pygame.transform.rotozoom(left_hand, 0, scale_factor)

center_x, center_y = WIDTH // 3.33, HEIGHT // 3.33

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    now = datetime.now()
    hours = now.hour % 12
    minutes = now.minute
    seconds = now.second

    sec_angle = -90 + (seconds / 60) * 360
    min_angle = -90 + (minutes / 60) * 360
    hour_angle = -90 + ((hours + minutes / 60) / 12) * 360  

    rotated_left = pygame.transform.rotozoom(left_hand, -sec_angle, 1) 
    rotated_right = pygame.transform.rotozoom(right_hand, -hour_angle, 1)

    left_rect = rotated_left.get_rect(center=(center_x, center_y))
    right_rect = rotated_right.get_rect(center=(center_x, center_y))
    screen.blit(rotated_left, left_rect)
    screen.blit(rotated_right, right_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

