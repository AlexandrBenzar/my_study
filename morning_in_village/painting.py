# -*- coding: utf-8 -*-

import simple_draw as sd
from canvas import smile, rainbow, tree, snowfall, house, sun

screen_width = 1500  # ширина экрана
screen_height = 600  # высота экрана
sd.resolution = (screen_width, screen_height)

point_for_tree = sd.get_point(1250, 0)
point_for_rainbow = sd.get_point(450, -130)

house.draw_house(start_of_wall=550, end_of_wall=950, height_of_wall=300)
tree.branch(point=point_for_tree, angle=90, length=90)

sd.take_background()

radius_for_rainbow = 1150
angle_of_rotation = 40
fps = 0

while not sd.user_want_exit():
    sd.start_drawing()
    snowfall.snowfall(start_of_snowfall=0, end_of_snowfall=500, height_of_snowfall=400)
    fps += 1
    if fps > 7:
        fps = 1

    rainbow.paint_rainbow(point=point_for_rainbow, radius=radius_for_rainbow, color_offset=fps % 7)
    smile.paint_smile(x=695, y=160, color=sd.COLOR_RED, radius_for_two_eye=fps + 4)

    angle_of_rotation = angle_of_rotation + 10
    if angle_of_rotation >= 360:
        angle_of_rotation = 0

    point_for_sun = sd.get_point(100, 500)
    sun.draw_sun(point_for_sun=point_for_sun, angle_of_rotation=angle_of_rotation)

    sd.sleep(0.1)
    sd.finish_drawing()

sd.pause()
