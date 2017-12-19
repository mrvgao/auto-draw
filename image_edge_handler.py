import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


def get_none_zero_x_y(img, canvas_width=None):
    img = cv2.imread(img,0)

    if canvas_width:
        system_size = canvas_width
        r = system_size / img.shape[1]
        dim = (system_size, int(img.shape[0] * r))
        img = cv2.resize(img, dim)

    edges = cv2.Canny(img, 80, 100)
    print(edges)
    none_zeros = np.nonzero(edges)
    pixels = [(x, y) for x, y in zip(none_zeros[1], none_zeros[0])]
    return pixels, edges


if __name__ == '__main__':
    import matplotlib; matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt

    plt.imshow(get_none_zero_x_y('imgs/cat01.jpg', canvas_width=1000)[1])
    plt.show()
