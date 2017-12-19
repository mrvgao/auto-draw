import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


def get_none_zero_x_y(img):
    img = cv2.imread(img,0)
    edges = cv2.Canny(img,100,200)
    print(edges)
    none_zeros = np.nonzero(edges)
    pixels = [(x, y) for x, y in zip(*none_zeros)]
    return pixels


