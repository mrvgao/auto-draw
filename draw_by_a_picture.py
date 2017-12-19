from mouse_handler import draw_by_sequence
from image_edge_handler import get_none_zero_x_y
import pyautogui as auto


def transfer_x_y(x, y, canvas_width_range, canvas_height_range):
    W, H = auto.size() # convert x in [0, W] to [canvas_width_range] y in [0, H] to [0, canvas_height_range]

    c_w = canvas_width_range
    c_h = canvas_height_range
    # set X' = a_wX + b_w
    # set Y' = a_hY + b_h

    b_w = c_w[0]
    a_w = (c_w[1] - c_w[0]) / W

    b_h = c_h[0]
    a_h = (c_h[1] - c_h[0]) / H

    return a_w * x + b_w, a_h * y + b_h


sequence = get_none_zero_x_y('imgs/cat01.png')
sequence = [transfer_x_y(x, y, [470, 1300], [150, 500]) for x, y in sequence]
print(sequence)
draw_by_sequence(sequence)
# draw_by_sequence('imgs/cat01.png')