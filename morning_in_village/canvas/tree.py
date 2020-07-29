# -*- coding: utf-8 -*-
import random
import simple_draw as sd


def branch(point, angle, length):
    if length < 7:
        return
    if length < 30:
        branch_tree = sd.vector(start=point, angle=angle, length=length, width=3, color=sd.COLOR_GREEN)
    else:
        branch_tree = sd.vector(start=point, angle=angle, length=length, width=3, color=(160, 82, 45))

    next_point_r = branch_tree
    next_angle_r = angle + random.randrange(18, 42)
    next_length_r = length * (random.randrange(60, 90) / 100)
    branch(point=next_point_r, angle=next_angle_r, length=next_length_r)
    next_point_l = branch_tree
    next_angle_l = angle - random.randrange(18, 42)
    next_length_l = length * (random.randrange(60, 90) / 100)
    branch(point=next_point_l, angle=next_angle_l, length=next_length_l)
