import sys
import math
import time

from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication


class Frame:

    def __init__(self, position, time):

        self.position = position
        self.time = time

    def speed(self, frame):

        d = distance(*self.position, *frame.position)

        time_delta = abs(frame.time - self.time)

        if time_delta == 0:

            return None

        else:

            return d / time_delta


def distance(x1, y1, x2, y2):

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_current_cursor_position():

    pos = QCursor.pos()

    return pos.x(), pos.y()


def get_current_frame():

    return Frame(get_current_cursor_position(), time.time())


if __name__ == '__main__':

    app = QApplication(sys.argv)

    screen = app.screens()[0]
    dpi = screen.physicalDotsPerInch()

    last_frame = get_current_frame()
    position_prev = get_current_cursor_position()

    while True:

        new_frame = get_current_frame()
        position_now = get_current_cursor_position()

        print(f'dpi={ dpi }, distance={ distance(position_prev[0], position_now[0], position_prev[1], position_prev[1])} , cursor: x={ position_now[0] },y={ position_now[1] }, speed={new_frame.speed(last_frame)}')
        last_frame = new_frame

        time.sleep(0.1)

        position_prev = get_current_cursor_position()
