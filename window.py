from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self._root = Tk() # Check args
        self._root.title("Maze Solver")
        self._canvas = Canvas(self._root, bg="white", height=height, width=width)
        self._canvas.pack(expand=1, fill=BOTH)
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
        print("Exiting the application.")

    def close(self):
        self._running = False