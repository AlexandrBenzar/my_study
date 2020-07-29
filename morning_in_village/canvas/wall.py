# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd


def paint_wall(start_of_wall, end_of_wall, height_of_wall, height_brick=60, width_brick=100):
    left_bottom_x, left_bottom_y, right_top_x, right_top_y = 0, 0, width_brick, 0

    for left_bottom_y in range(0, height_of_wall, height_brick):
        right_top_y = right_top_y + height_brick

        x_offset = start_of_wall if (right_top_y % (height_brick * 2)) else start_of_wall + round(width_brick / 2)
        right_top_x = end_of_wall if (right_top_y % (height_brick * 2)) else end_of_wall + round(width_brick / 2)

        for left_bottom_x in range(x_offset, end_of_wall, width_brick):
            left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
            right_top = sd.get_point(right_top_x, right_top_y)
            sd.rectangle(left_bottom, right_top, width=2)
