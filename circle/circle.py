import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Move")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
move_distance = 20

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP and ball_y - move_distance - ball_radius >= 0:
                ball_y -= move_distance
            elif event.key == pygame.K_DOWN and ball_y + move_distance + ball_radius <= HEIGHT:
                ball_y += move_distance
            elif event.key == pygame.K_LEFT and ball_x - move_distance - ball_radius >= 0:
                ball_x -= move_distance
            elif event.key == pygame.K_RIGHT and ball_x + move_distance + ball_radius <= WIDTH:
                ball_x += move_distance

    screen.fill(WHITE)  
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)  
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()
