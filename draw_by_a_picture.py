from mouse_handler import draw_by_sequence
from image_edge_handler import get_none_zero_x_y
from utilities import transfer_x_y
import pyautogui as auto


sequence = get_none_zero_x_y('imgs/cat03.jpg')
sequence = [transfer_x_y(x, y, [294, 945], [257, 618]) for x, y in sequence]
#sequence = [(y, x) for x, y in sequence]
print(len(sequence))
auto.PAUSE = 1.0
draw_by_sequence(sequence)
print('draw done')
# draw_by_sequence('imgs/cat01.png')