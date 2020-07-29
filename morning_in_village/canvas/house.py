import simple_draw as sd
from canvas import wall


def draw_house(start_of_wall, end_of_wall, height_of_wall, height_brick=50):

    wall.paint_wall(start_of_wall=start_of_wall, end_of_wall=end_of_wall,
                    height_of_wall=height_of_wall, height_brick=height_brick)
    point_for_wall = sd.get_point(start_of_wall, 0)
    sd.vector(start=point_for_wall, angle=90, length=height_of_wall)
    point_for_wall = sd.get_point(end_of_wall+height_brick, 0)
    sd.vector(start=point_for_wall, angle=90, length=height_of_wall)

    point_for_window_left_bottom = sd.get_point((end_of_wall-start_of_wall)/2+start_of_wall-150, 100)
    point_for_window_right_top = sd.get_point((end_of_wall-start_of_wall)/2+start_of_wall+50, height_of_wall-50)
    sd.rectangle(point_for_window_left_bottom, point_for_window_right_top, width=0, color=sd.COLOR_BLUE)
    list_for_roof = [sd.get_point(start_of_wall-50, height_of_wall),
                     sd.get_point(end_of_wall+100, height_of_wall),
                     sd.get_point((end_of_wall-start_of_wall)/2+start_of_wall, height_of_wall+100)]
    sd.polygon(point_list=list_for_roof, color=sd.COLOR_BLUE, width=0)
