import pyautogui as auto
from scipy.spatial.distance import euclidean


def move_and_click(position):
    x, y = position
    auto.moveTo(x, y, duration=.0)
    auto.click(x, y, duration=.0)


def draw_by_sequence(coornidations):
    threshold = 0.0

    def distance(x1, y1, x2, y2): return euclidean((x1, y1), (x2, y2))

    start_position = coornidations[0]
    move_and_click(start_position)

    for i in range(1, len(coornidations)):
        if distance(*coornidations[i-1], *coornidations[i]) < threshold:
            auto.dragTo(coornidations[i])
        else:
            move_and_click(coornidations[i])


if __name__ == '__main__':
    test_positions = [(1, 2), (30, 40), (400, 500)]
    draw_by_sequence(test_positions)


