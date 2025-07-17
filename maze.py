from __future__ import annotations

from window import Window, Line, Point
from time import sleep


class Maze:
    def __init__(self, x1 : int, y1 : int, num_cols : int, num_rows : int, cell_size : int, window : Window | None = None):
        self._window = window
        self._x1 = x1
        self._y1 = y1
        self._num_cols = num_cols
        self._num_rows = num_rows
        self._cell_size = cell_size
        self._cells = []
        self._create_cells()


    def _create_cells(self):
        for x in range(self._num_cols):
            self._cells.append([])
            for y in range(self._num_rows):
                self._cells[x].append(Cell(self._window))
                self._draw_cell(x, y)
                self._animate()

    def _draw_cell(self, x : int, y : int):
        self._cells[x][y].draw(
            (self._x1 + x * self._cell_size),
            (self._y1 + y * self._cell_size),
            self._cell_size
        )

    def _animate(self):
        if self._window == None:
            return
        
        self._window.redraw()
        sleep(0.05)


class Cell:
    def __init__(self, window : Window | None = None):
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
        if self._window == None:
            return
        
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

    def draw_path_to(self, to_cell : Cell, undo : bool = False):
        if self._window == None:
            return
        
        color = "red" if not undo else "gray"

        self._window.draw_line(Line(
            Point(int((self._x1 + self._x2)/2), int((self._y1 + self._y2)/2)), 
            Point(int((to_cell._x1 + to_cell._x2)/2), int((to_cell._y1 + to_cell._y2)/2))
        ), fill_color=color)
