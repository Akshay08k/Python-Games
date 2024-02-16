import pygame
import time
import random

pygame.init()


width = 800 
height = 600


black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)


game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

snake_x = [width / 2]
snake_y = [height / 2]
snake_size = 10
snake_length = 1

dx = 0
dy = 0


food_x = random.randrange(0, width - snake_size, snake_size)
food_y = random.randrange(0, height - snake_size, snake_size)


score = 0

font = pygame.font.Font(None, 36)


game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -snake_size
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = snake_size
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -snake_size
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = snake_size

    x = snake_x[-1] + dx
    y = snake_y[-1] + dy

 
    if x == food_x and y == food_y:
        score += 1
        food_x = random.randrange(0, width - snake_size, snake_size)
        food_y = random.randrange(0, height - snake_size, snake_size)
        snake_length += 1

    
    snake_x.append(x)
    snake_y.append(y)

  
    if len(snake_x) > snake_length:
        del snake_x[0]
        del snake_y[0]

    game_display.fill(black)

  
    pygame.draw.rect(game_display, red, [food_x, food_y, snake_size, snake_size])

    for i in range(snake_length):
        pygame.draw.rect(
            game_display, red, [snake_x[i], snake_y[i], snake_size, snake_size]
        )

  
    text = font.render(f'Points: {score}', True, white)
    game_display.blit(text, (width - 150, 10))


    if (
        x >= width
        or x < 0
        or y >= height
        or y < 0
        or (x, y) in zip(snake_x[:-1], snake_y[:-1])  # Exclude the last segment
    ):
        game_over = True

 
    pygame.display.update()


    time.sleep(0.1)

# Game over message
game_display.fill(black)
game_over_text = font.render('Game Over', True, red)
game_display.blit(game_over_text, (width / 2 - 100, height / 2 - 50))
score_text = font.render(f'Your Score: {score}', True, white)
game_display.blit(score_text, (width / 2 - 100, height / 2 + 20))
pygame.display.update()

# Wait for a few seconds before quitting
time.sleep(2)

pygame.quit()
