import pyautogui as auto
from scipy.spatial.distance import euclidean
from tqdm import tqdm


def move_and_click(position):
    x, y = position
    auto.moveTo(x, y, duration=.0)
    auto.click(x, y, duration=.0)


def draw_by_sequence(coornidations):
    threshold = 10

    auto.PAUSE = 9 / len(coornidations)

    def distance(x1, y1, x2, y2): return euclidean((x1, y1), (x2, y2))

    start_position = coornidations[0]
    move_and_click(start_position)

    for i in tqdm(range(1, len(coornidations)), total=len(coornidations)):
        # if i % 10 != 0: continue
        if coornidations[i-1] is None or coornidations[i] is None: break
        dis = distance(*coornidations[i-1], *coornidations[i])
        # print(dis)
        if dis > threshold:
            # print('move: {}'.format(coornidations[i]))
            move_and_click(coornidations[i])
        else:
            # print('drag: {}'.format(coornidations[i]))
            K = 50
            duration = distance(*coornidations[i-1], *coornidations[i]) / K
            auto.dragTo(*coornidations[i], duration, button='left')


if __name__ == '__main__':
    test_positions = [(1, 2), (30, 40), (400, 500)]
    draw_by_sequence(test_positions)


