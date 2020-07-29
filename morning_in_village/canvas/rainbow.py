import simple_draw as sd

STEP = 7

RAINBOW_COLORS = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]


def paint_rainbow(point, radius, color_offset):
    colors = RAINBOW_COLORS[color_offset:] + RAINBOW_COLORS[:color_offset]
    for color_rainbow in colors:
        color = color_rainbow
        sd.circle(center_position=point, radius=radius, color=color, width=6)
        radius = radius + STEP
