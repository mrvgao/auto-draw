from mouse_handler import draw_by_sequence
from image_edge_handler import get_none_zero_x_y
from utilities import transfer_x_y
import pyautogui as auto
import os
import random
import sys


def sort_sequence(sequence, sample=0.1):
    ## sort sequence by nearest point first order
    # random_begin_point = random.choice(sequence)
    random_begin_point = random.choice(sequence[:100])

    random.shuffle(sequence)
    sequence = sequence[: int(len(sequence) * sample)]

    # points = {p: True for p in sequence}
    points = set(sequence)
    # points[random_begin_point] = False

    def distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
        #return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def get_nearest(p, points):
        threshold = 5
        min_distance, min_p = float('inf'), None
        for tmp_p in points:
            if tmp_p == p: continue

            dis = distance(*p, *tmp_p)
            if dis < threshold: min_p = tmp_p; break
            elif dis < min_distance:
                min_distance = dis
                min_p = tmp_p
        return min_p

    current_p = random_begin_point

    sorted_result = [random_begin_point]

    while len(points) > 0:
        # existed_points = [_p for _p in points if points[_p]]
        print(len(points))
        if current_p is None: break
        nearest_point = get_nearest(current_p, points)
        sorted_result.append(nearest_point)
        if current_p != random_begin_point:
            points.remove(current_p)
        current_p = nearest_point
        # points[nearest_point] = False

    return sorted_result


x_range = [629, 1267]
y_range = [270, 620]

dir = './imgs'
# filename = random.choice(os.listdir(dir))
filename = 'cat01.jpg'
pixels = get_none_zero_x_y(os.path.join(dir, filename), 1500)

sequence = pixels[0]

max_y, max_x = pixels[1].shape
sequence = [transfer_x_y(x, y, x_range, y_range, max_x, max_y) for x, y in sequence]
sequence = [(x, y) for x, y in sequence]
print(len(sequence))
sequence = sort_sequence(sequence, sample=0.4)
print(len(sequence))
auto.PAUSE = 1.0
draw_by_sequence(sequence)
print('draw done')
# draw_by_sequence('imgs/cat01.png')
sys.exit(-1)