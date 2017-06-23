import pygame
import sys
from pygame.locals import *
from Player import Player
from Bubble import Bubble

# initialize the session
pygame.init()

# general display settings
screen = pygame.display.set_mode((640,460))
pygame.display.set_caption("Bubble Buster!")
screen.fill((255, 255, 255))
font = pygame.font.SysFont(None, 36)

backg = pygame.image.load("images/floor.jpg").convert_alpha()
backg = pygame.transform.scale(backg, (640, 460))

main_clock = pygame.time.Clock()

# player display settings
player = Player()
player.rect.x = 250
player_speed = player.speed

draw_group = pygame.sprite.Group()
draw_group.add(player)

bubble_group = pygame.sprite.Group()

# bubble display settings
all_bubbles = [ ]
bubble_radius = 20
bubble_edge = 1
initial_bubble_position = 70
bubble_spacing = 60

# game play variables
move_left = False
move_right = False
x_position = 380
y_position = 320
last_x = x_position
last_y = y_position
ball_can_move = False
speed = [5, -5]
score = 0
lives = 3
alive = True
number_of_bubbles = 30


def draw_player():
    pygame.draw.rect(screen, (0, 0, 0), player)

def draw_screen():
    screen.fill((255, 255, 255))

def create_bubbles():
    bubble_x = initial_bubble_position
    bubble_y = initial_bubble_position
    for rows in range (0, 3):
        for columns in range (0, 10):
            bubble = Bubble(bubble_x - 30, bubble_y)
            bubble_group.add(bubble)
            bubble_x += bubble_spacing
            all_bubbles.append(bubble)
        bubble_y += bubble_spacing
        bubble_x = initial_bubble_position

create_bubbles()

def draw_bubbles():
    for bubble in bubble_group:
        bubble = pygame.draw.circle((screen), (0, 0, 0), (bubble.rect.x, bubble.rect.y), bubble_radius, bubble_edge)

def draw_text(display_string, font, surface, x, y):
    text_display = font.render(display_string, 1, (0, 0, 0))
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # keyboard input for players
        if event.type == KEYDOWN:
            if event.key == K_a:
                move_right = False
                move_left = True
            if event.key == K_d:
                move_right = True
                move_left = False
        if event.type == KEYUP:
            if event.key == K_a:
                move_left = False
            if event.key == K_d:
                move_right = False
            if alive:
                if event.key == K_SPACE:
                    ball_can_move = True
            if True:#not alive:
                if event.key == K_RETURN:
                    lives = 3
                    alive = True
                    score = 0
                    ball_can_move = False
                    number_of_bubbles = 30
                    bubble_group.empty()
                    create_bubbles()
                    draw_screen()
                    draw_group.draw(screen)
                    bubble_group.draw(screen)
                    pygame.display.update()

    main_clock.tick(50)

    if move_left and player.rect.left > 0:
        player.rect.x -= player_speed
    if move_right and player.rect.right < 640:
        player.rect.x += player_speed

    if ball_can_move:
        last_x = x_position
        last_y = y_position

        x_position += speed[0]
        y_position += speed[1]
        if ball.y <= 0:
            y_position = 15
            speed[1] = -speed[1]
        elif ball.y >= 460:
            lives -= 1
            ball_can_move = False
        if ball.x <= 0:
            x_position = 15
            speed[0] = -speed[0]
        if ball.x >= 640:
            x_position = 625
            speed[0] = -speed[0]
        # Test collisions with the player
        if ball.colliderect(player):
            y_position -= 15
            speed[1] = -speed[1]
        # Move direction
        move_direction = ((x_position - last_x), (y_position - last_y))

        # Test collisions with the bubbles
        for bubble in bubble_group:
            if ball.colliderect(bubble.rect):
                if move_direction[1] > 0:
                    speed[1] = -speed[1]
                    y_position -= 10
                elif move_direction[1] < 0:
                    speed[1] = -speed[1]
                    y_position += 10
                bubble_group.remove(bubble)
                number_of_bubbles -= 1
                score += 100
                break
    else:
        x_position = player.rect.x + 30
        y_position = 380

    if lives <= 0:
        alive = False

    draw_screen()
    screen.blit(backg, (0,0))
    draw_group.draw(screen)
    bubble_group.draw(screen)
    
    ball = pygame.draw.circle(screen, (255, 200, 0), (x_position, y_position), 5, 0)

    if alive:
        draw_text('Score: %s' % (score), font, screen, 5, 5)
        draw_text('Lives: %s' % (lives), font, screen, 540, 5)
        if not number_of_bubbles:
            draw_text('You Win!!', font, screen, 255, 5)
            draw_text('Press Enter to Play Again', font, screen, 180, 50)
    elif not alive and number_of_bubbles:
        draw_text('Game Over', font, screen, 255, 5)
        draw_text('Press Enter to Play Again', font, screen, 180, 50)
    elif not alive and not number_of_bubbles:
        draw_text('You Win!!', font, screen, 255, 5)
        draw_text('Press Enter to Play Again', font, screen, 180, 50)

    pygame.display.update()
