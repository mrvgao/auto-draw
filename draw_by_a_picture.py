from mouse_handler import draw_by_sequence
from image_edge_handler import get_none_zero_x_y
from utilities import transfer_x_y
import pyautogui as auto
import os
import random


def sort_sequence(sequence, sample=0.2):
    ## sort sequence by nearest point first order
    # random_begin_point = random.choice(sequence)
    random_begin_point = sequence[0]

    random.shuffle(sequence)
    sequence = sequence[: int(len(sequence) * sample)]

    points = {p: True for p in sequence}
    points[random_begin_point] = False

    def distance(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def get_nearest(p, points):
        min_distance, min_p = distance(*p, *points[0]), points[0]
        for tmp_p in points:
            if tmp_p == p: continue

            dis = distance(*p, *tmp_p)
            if dis < min_distance:
                min_distance = dis
                min_p = tmp_p
        return min_p

    current_p = random_begin_point

    sorted_result = [current_p]
    while len([_ for _ in points if points[_]]) > 0:
        existed_points = [_p for _p in points if points[_p]]
        print(len(existed_points))
        nearest_point = get_nearest(current_p, existed_points)
        sorted_result.append(nearest_point)
        current_p = nearest_point
        points[nearest_point] = False

    return sorted_result


sequence = get_none_zero_x_y('imgs/cat03.jpg')
sequence = [transfer_x_y(x, y, [390, 1040], [270, 620]) for x, y in sequence]
sequence = [(x, y) for x, y in sequence]
sequence = sort_sequence(sequence)
print(len(sequence))
auto.PAUSE = 1.0
draw_by_sequence(sequence)
print('draw done')
# draw_by_sequence('imgs/cat01.png')