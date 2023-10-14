import pygame
import random
import time
import math

pygame.init()

window_size = (1280, 720)
pygame.display.set_caption("Monkey Kong")

screen = pygame.display.set_mode(window_size)
font = pygame.font.Font(None, 36)

background_image = pygame.image.load("../image/background.png")
hero_image = pygame.image.load("../image/hero.png")
wood_image = pygame.image.load("../image/wood.png")
monkey_image = pygame.image.load("../image/monkey.png")
ball_image = pygame.image.load("../image/ball.png")

background_image = pygame.transform.scale(background_image, window_size)

wood_width = window_size[0]
wood_height = 100
wood_image = pygame.transform.scale(wood_image, (wood_width, wood_height))
wood_pos = [0, window_size[1] * 0.8]
upper_wood_pos = [0, 0]

monkey_width = window_size[0] // 10
monkey_height = monkey_image.get_height() * monkey_width // monkey_image.get_width()
monkey_image = pygame.transform.scale(monkey_image, (monkey_width, monkey_height))
monkey_x = random.randint(0, window_size[0] - monkey_width)
monkey_y = upper_wood_pos[1] + wood_height
monkey_direction = 1

hero_width = window_size[0] // 18
hero_height = hero_image.get_height() * hero_width // hero_image.get_width()
hero_image = pygame.transform.scale(hero_image, (hero_width, hero_height))
hero_x = window_size[0] / 2 - hero_width / 2
hero_y = wood_pos[1] - hero_height

ball_width = (window_size[0] // 20) // 2  # размер уменьшен в 2 раза
ball_height = (ball_image.get_height() * ball_width // ball_image.get_width())
ball_image = pygame.transform.scale(ball_image, (ball_width, ball_height))
balls = []

hero_speed = 1
monkey_speed = 2 / 3
jump_power = 4
gravity = 0.05
ball_speed = 2 / 2
ball_frequency = 4 / 3

hero_jump = False
hero_speed_y = 0

score = 0
last_ball_time = time.time()
multiplier = 1
next_level_score = 10

run = True
while run:
    screen.blit(background_image, (0, 0))
    screen.blit(wood_image, wood_pos)
    screen.blit(wood_image, upper_wood_pos)
    screen.blit(hero_image, (hero_x, hero_y))
    screen.blit(monkey_image, (monkey_x, monkey_y))

    score_display = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_display, (10, 100))

    if score >= next_level_score:
        next_level_score += 10
        multiplier += 0.2
        ball_speed *= multiplier
        ball_frequency /= multiplier

    monkey_x += monkey_speed * monkey_direction
    if monkey_x + monkey_width > window_size[0] or monkey_x < 0:
        monkey_direction *= -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if not hero_jump:
                    hero_jump = True
                    hero_speed_y = -jump_power

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        hero_x -= hero_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        hero_x += hero_speed

    hero_x = max(0, hero_x)
    hero_x = min(window_size[0] - hero_width, hero_x)

    if hero_jump:
        hero_y += hero_speed_y
        hero_speed_y += gravity
        if hero_y > wood_pos[1] - hero_height:
            hero_y = wood_pos[1] - hero_height
            hero_jump = False

    if time.time() - last_ball_time >= ball_frequency:
        last_ball_time = time.time()
        for i in range(int(multiplier)):
            dx = hero_x - monkey_x
            dy = hero_y - monkey_y
            direction = math.atan2(dy, dx)
            balls.append({'x': monkey_x, 'y': monkey_y, 'dx': math.cos(direction) * ball_speed,
                          'dy': math.sin(direction) * ball_speed})

    for ball in balls[:]:
        ball['x'] += ball['dx']
        ball['y'] += ball['dy']
        if ball['y'] <= wood_height or ball['y'] >= wood_pos[1] - ball_height:
            ball['dy'] *= -1

        ball_rect = pygame.Rect(ball['x'], ball['y'], ball_width, ball_height)
        hero_rect = pygame.Rect(hero_x, hero_y, hero_width, hero_height)

        if ball['x'] < 0 or ball['x'] > window_size[0] - ball_width:
            score += 1
            balls.remove(ball)
        elif ball_rect.colliderect(hero_rect):
            run = False
        else:
            screen.blit(ball_image, (ball['x'], ball['y']))

    pygame.display.update()

pygame.quit()
