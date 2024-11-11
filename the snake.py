import pygame
import random

pygame.init()

screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Snake")

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 35)

def message(msg, color, position):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, position)

def display_score(score):
    value = score_font.render("Score: " + str(score), True, blue)
    screen.blit(value, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    x1, y1 = screen_width / 2, screen_height / 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1
    score = 0

    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    clock = pygame.time.Clock()
    while not game_over:
        while game_close:
            screen.fill(black)
            message("Game Over!", red, (screen_width / 4 + 50, screen_height / 3))
            message("1 - To try again, press A.", red, (screen_width / 4, screen_height / 3 + 40))
            message("2 - To exit, press Q.", red, (screen_width / 4, screen_height / 3 + 80))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        for x in snake_list:
            pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 10

        display_score(score)
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
