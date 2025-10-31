import pygame
import sys
import os

pygame.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

BASE_DIR = os.path.dirname(__file__)
IMG_DIR = os.path.join(BASE_DIR, "imgs")
MUSIC_DIR = os.path.join(BASE_DIR, "music")

WHITE = (255, 255, 255)

background = pygame.image.load(os.path.join(IMG_DIR, "background.png")).convert()

scale_factor_bg = 0.5
bg_width = int(background.get_width() * scale_factor_bg)
bg_height = int(background.get_height() * scale_factor_bg)
background = pygame.transform.scale(background, (bg_width, bg_height))

bg_x = (WIDTH - bg_width) // 2
bg_y = (HEIGHT - bg_height) // 2
play_img = pygame.image.load(os.path.join(IMG_DIR, "play.png")).convert_alpha()
stop_img = pygame.image.load(os.path.join(IMG_DIR, "stop.png")).convert_alpha()
next_img = pygame.image.load(os.path.join(IMG_DIR, "next.png")).convert_alpha()
prev_img = pygame.image.load(os.path.join(IMG_DIR, "prev.png")).convert_alpha()

scale_factor = 0.1
play_img = pygame.transform.rotozoom(play_img, 0, scale_factor)
stop_img = pygame.transform.rotozoom(stop_img, 0, scale_factor)
next_img = pygame.transform.rotozoom(next_img, 0, scale_factor)
prev_img = pygame.transform.rotozoom(prev_img, 0, scale_factor)

button_gap = 20
total_width = (
    play_img.get_width()
    + stop_img.get_width()
    + next_img.get_width()
    + prev_img.get_width()
    + button_gap * 3
)

start_x = (WIDTH - total_width) // 1.5
button_y = (HEIGHT - play_img.get_height()) // 1.5

positions = {
    "prev": (start_x, button_y),
    "play": (start_x + prev_img.get_width() + button_gap, button_y),
    "stop": (start_x + prev_img.get_width() + play_img.get_width() + button_gap * 2, button_y),
    "next": (start_x + prev_img.get_width() + play_img.get_width() + stop_img.get_width() + button_gap * 3, button_y),
}

tracks = [os.path.join(MUSIC_DIR, f) for f in os.listdir(MUSIC_DIR) if f.endswith(".mp3")]
tracks.sort()
current_track = 0

pygame.mixer.music.load(tracks[current_track])
playing = False

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))

    screen.blit(prev_img, positions["prev"])
    screen.blit(play_img, positions["play"])
    screen.blit(stop_img, positions["stop"])
    screen.blit(next_img, positions["next"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: 
                pygame.mixer.music.play()
                playing = True

            elif event.key == pygame.K_s:  
                pygame.mixer.music.stop()
                playing = False

            elif event.key == pygame.K_d: 
                current_track = (current_track + 1) % len(tracks)
                pygame.mixer.music.load(tracks[current_track])
                pygame.mixer.music.play()
                playing = True

            elif event.key == pygame.K_a: 
                current_track = (current_track - 1) % len(tracks)
                pygame.mixer.music.load(tracks[current_track])
                pygame.mixer.music.play()
                playing = True

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
