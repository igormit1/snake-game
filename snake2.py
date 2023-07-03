import pygame as pgg
from random import randrange

window = 500
tile = 30
RANGE = (tile // 2, window - tile // 2, tile)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pgg.rect.Rect([0, 0, tile - 2, tile - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 110
tela = pgg.display.set_mode([window] * 2)
clock = pgg.time.Clock()
dirs = {pgg.K_w: 1, pgg.K_s: 1, pgg.K_a: 1, pgg.K_d: 1}
food = snake.copy()
food.center = get_random_position()

while True:
    for event in pgg.event.get():
        if event.type == pgg.QUIT:
            exit()
        if event.type == pgg.KEYDOWN:
            if event.key == pgg.K_w and dirs[pgg.K_w]:
                snake_dir = (0, -tile)
                dirs = {pgg.K_w: 1, pgg.K_s: 0, pgg.K_a: 1, pgg.K_d: 1}
            if event.key == pgg.K_s and dirs[pgg.K_s]:
                snake_dir = (0, tile)
                dirs = {pgg.K_w: 0, pgg.K_s: 1, pgg.K_a: 1, pgg.K_d: 1}
            if event.key == pgg.K_a and dirs[pgg.K_a]:
                snake_dir = (-tile, 0)
                dirs = {pgg.K_w: 1, pgg.K_s: 1, pgg.K_a: 1, pgg.K_d: 0}
            if event.key == pgg.K_d and dirs[pgg.K_d]:
                snake_dir = (tile, 0)
                dirs = {pgg.K_w: 1, pgg.K_s: 1, pgg.K_a: 0, pgg.K_d: 1}
    tela.fill('green')
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1
    [pgg.draw.rect(tela, 'red', segment) for segment in segments]
    time_now = pgg.time.get_ticks()
    pgg.draw.rect(tela, 'yellow', food)
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
        self_eating = snake.collidelist(segments[:-1]) != -1
        if (
            snake.left < 0
            or snake.right > window
            or snake.top < 0
            or snake.bottom > window
            or self_eating
        ):
            snake.center, food.center = get_random_position(), get_random_position()
            length, snake_dir = 1, (0, 0)
            segments = [snake.copy()]
    pgg.display.flip()
    clock.tick(60)