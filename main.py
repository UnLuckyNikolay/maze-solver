from time import sleep

from constants import *
from window import Window
from maze import Maze


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    sleep(0.2)
    while window._running:
        #maze = Maze(MAZE_X, MAZE_Y, 3, 3, CELL_SIZE, window) # TEST
        maze = Maze(MAZE_X, MAZE_Y, MAZE_COLUMNS, MAZE_ROWS, CELL_SIZE, window)
        maze.solve()
        interruptible_sleep(window, RESTART_DELAY)
        window._canvas.delete("all")
    window.wait_for_close()

def interruptible_sleep(window : Window, seconds):
    tens = int(seconds // 0.1)
    for i in range(tens):
        sleep(0.1)
        window.redraw()
        if not window._running:
            return


if __name__ == "__main__":
    main()