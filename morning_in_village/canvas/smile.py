# -*- coding: utf-8 -*-

import simple_draw as sd


def paint_smile(x, y, radius_for_two_eye, color=sd.COLOR_YELLOW):
    central_point_head = sd.get_point(x, y)
    central_point_eye_1 = sd.get_point(x - 20, y + 25)
    central_point_eye_2 = sd.get_point(x + 20, y + 25)
    point_smile_1 = sd.get_point(x - 40, y - 20)
    point_smile_2 = sd.get_point(x - 35, y - 25)
    point_smile_3 = sd.get_point(x + 35, y - 25)
    point_smile_4 = sd.get_point(x + 40, y - 20)

    sd.lines((point_smile_1, point_smile_2, point_smile_3, point_smile_4), color, False, 4)
    sd.circle(central_point_head, 60, color, 4)

    sd.circle(center_position=central_point_eye_1, radius=12, color=sd.COLOR_BLUE, width=0)
    sd.circle(center_position=central_point_eye_2, radius=12, color=sd.COLOR_BLUE, width=0)

    radius_for_two_eye %= 12

    sd.circle(center_position=central_point_eye_1, radius=radius_for_two_eye, color=color, width=0)
    sd.circle(center_position=central_point_eye_2, radius=radius_for_two_eye, color=color, width=0)
