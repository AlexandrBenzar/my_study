import simple_draw as sd

ANGLE_BETWEEN_RAYS = 60


def draw_sun(point_for_sun, angle_of_rotation):
    length = 100

    sd.circle(center_position=point_for_sun, radius=105, color=sd.background_color, width=0)

    sd.circle(center_position=point_for_sun, radius=50, color=sd.COLOR_YELLOW, width=0)

    for angle in range(angle_of_rotation, 360 + angle_of_rotation, ANGLE_BETWEEN_RAYS):
        sd.vector(start=point_for_sun, angle=angle, length=length, color=sd.COLOR_YELLOW, width=3)
