from window import Window, Line, Point


class Cell:
    def __init__(self, window : Window):
        self.has_upper_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self._x1 = -1
        self._x2 = -1
        self._y1 = -1
        self._y2 = -1
        self._window = window
    
    def draw(self, x1, y1, size):
        self._x1 = x1
        self._x2 = x1 + size
        self._y1 = y1
        self._y2 = y1 + size

        if self.has_upper_wall:
            self._window.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        if self.has_right_wall:
            self._window.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        if self.has_bottom_wall:
            self._window.draw_line(Line(Point(self._x2, self._y2), Point(self._x1, self._y2)))
        if self.has_left_wall:
            self._window.draw_line(Line(Point(self._x1, self._y2), Point(self._x1, self._y1)))
