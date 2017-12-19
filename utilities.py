import pyautogui as auto
from image_edge_handler import get_none_zero_x_y
import numpy as np
import random


def transfer_x_y(x, y, canvas_width_range, canvas_height_range, r=False):
    W, H = auto.size() # convert x in [0, W] to [canvas_width_range] y in [0, H] to [0, canvas_height_range]

    c_w = canvas_width_range
    c_h = canvas_height_range
    # set X' = a_wX + b_w
    # set Y' = a_hY + b_h

    def random_move(length_range):
        move = random.randint(-5, 5)
        return length_range[0] + move, length_range[1] + length_range[1]

    def random_resize(length_range):
        resize = 1
        return length_range[0] * resize, length_range[1] * resize

    if r:
        c_w = random_resize(random_move(c_w))
        c_h = random_resize(random_move(c_h))

    b_w = c_w[0]
    a_w = (c_w[1] - c_w[0]) / W

    b_h = c_h[0]
    a_h = (c_h[1] - c_h[0]) / H

    new_x = int(round(a_w * y + b_w))
    new_y = int(round(a_h * x + b_h))

    new_x = min(canvas_width_range[1], max(canvas_width_range[0], new_x))
    new_y = min(canvas_height_range[1], max(canvas_height_range[0], new_y))

    assert canvas_width_range[0] <= new_x <= canvas_width_range[1]
    assert canvas_height_range[0] <= new_y <= canvas_height_range[1]

    return new_x, new_y


if __name__ == '__main__':
    import matplotlib; matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt

    positions = get_none_zero_x_y('imgs/cat01.png')

    w_range = [294, 945]
    h_range = [257, 618]

    img_array = np.zeros((w_range[1], h_range[1]))

    for x, y in positions:
        x, y = transfer_x_y(x, y, w_range, h_range)
        img_array[x][y] = 1

    plt.imshow(img_array)
    plt.show()





