import pygame
import random

pygame.init()

SCREEN = pygame.display.set_mode((500, 750))
BACKGROUND_IMAGE = pygame.image.load("background (2).jpg")
BIRD_IMAGE = pygame.image.load('bird1.png')
bird_x = 50
bird_y = 350
bird_y_change = 0

def display_bird(x, y):
    SCREEN.blit(BIRD_IMAGE, (x, y))


OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150, 450)
OBSTACLE_COLOR = (200, 250, 100)
OBSTACLE_X_CHANGE = -1
obstacle_x = 500


def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_y = height + 200
    bottom_height = 635 - bottom_y
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, bottom_y, OBSTACLE_WIDTH, bottom_height))


start_font = pygame.font.Font("freesansbold.ttf", 32)
def start():
    display = start_font.render(f'PRESS SPACE BAR TO START', True, (225, 225, 225))
    SCREEN.blit(display, (10, 100))
    pygame.display.update()


game_over_font1 = pygame.font.Font("freesansbold.ttf", 64)
game_over_font2 = pygame.font.Font("freesansbold.ttf", 32)


def game_over():
    display1 = game_over_font1.render(f'GAME OVER', True, (100, 0, 0))
    SCREEN.blit(display1, (40, 300))
    display2 = game_over_font2.render(f'Score:{score}', True, (225, 225, 225))
    SCREEN.blit(display2, (10, 400))
    pygame.display.update()


score = 0
score_font = pygame.font.Font("freesansbold.ttf", 32)

def score_display(score):
    display = score_font.render(f'Score:{score}', True, (225, 225, 100))
    SCREEN.blit(display, (300, 10))
    pygame.display.update()


def collision_detection(obstacle_x, obstacle_height, bird_y, bottom_obstacle_height):
    if 50 <= obstacle_x <= (50 + 64):
        if bird_y <= obstacle_height or bottom_obstacle_height <= bird_y:
            return True
    return False


running = True
waiting = True
collision = False
while running:
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

    while waiting:
        if collision:
            game_over()
            start()
            collision = False

        else:
            start()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        score = 0
                        bird_y = 300
                        obstacle_x = 500
                        waiting = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = 0.5

    bird_y += bird_y_change
    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 571:
        bird_y = 571

    obstacle_x += OBSTACLE_X_CHANGE
    collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, bird_y, OBSTACLE_HEIGHT + 200)

    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(150, 450)
        score += 1
    display_obstacle(OBSTACLE_HEIGHT)
    display_bird(bird_x, bird_y)
    score_display(score)
    if collision:
        waiting = True

    pygame.display.update()
pygame.quit()
