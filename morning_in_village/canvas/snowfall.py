# -*- coding: utf-8 -*-

import random
import simple_draw as sd

snowflake = []
fallen_snowflakes = []
quantity_of_snowflakes = 200
for _ in range(quantity_of_snowflakes):
    rand_int = random.randrange(5, 15, 5)
    rand_x = random.randrange(50, 500, 50)
    rand_y = random.randrange(200, 400, 50)
    snowflake.append({'x': rand_x, 'y': rand_y, 'size': rand_int})


def snowfall(start_of_snowfall, end_of_snowfall, height_of_snowfall=400):
    # закрасили все снежинки цветом фона
    for elem in snowflake:
        point = (sd.get_point(elem['x'], elem['y']))
        sd.snowflake(center=point, length=elem['size'], color=sd.background_color)
    # изменяем положение всех снежинок (делаем с ними, что хотим, т.к. сейчас экран чистый, все снежинки закрашены)
    # в том числе, упавшие снежинки поднимаем на самый верх.
    for elem in snowflake:
        elem['y'] -= 10
        elem['x'] += random.randrange(-10, 10)
        if elem['y'] < elem['size']:
            fallen_snowflakes.append(dict(elem))
            elem['y'] = random.randrange(200, height_of_snowfall, 50)
            elem['x'] = random.randrange(start_of_snowfall, end_of_snowfall, 50)
    # красим все снежинк белым цветом, теперь они появляются на экране.
    for elem in snowflake + fallen_snowflakes:
        point = (sd.get_point(elem['x'], elem['y']))
        sd.snowflake(center=point, length=elem['size'], color=sd.COLOR_WHITE)

    while len(fallen_snowflakes) > 200:
        oldest_snowflake = fallen_snowflakes[0]
        point = (sd.get_point(oldest_snowflake['x'], oldest_snowflake['y']))
        sd.snowflake(center=point, length=oldest_snowflake['size'], color=sd.background_color)
        del fallen_snowflakes[0]
