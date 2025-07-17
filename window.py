from __future__ import annotations

from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width : int, height : int):
        self._root = Tk() # Check args
        self._root.title("Maze Solver")
        self._canvas = Canvas(self._root, bg="white", height=height, width=width)
        self._canvas.pack(expand=1, fill=BOTH)
        self._running = True
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        while self._running:
            self.redraw()
        print("Exiting the application.")

    def close(self):
        self._running = False
        self._root.quit()

    def draw_line(self, line : Line, fill_color : str = "black"):
        line.draw(self._canvas, fill_color=fill_color)

class Point:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1 : Point, point2 : Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas : Canvas, fill_color : str):
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill=fill_color, width=2
        )