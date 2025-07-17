from time import sleep

from constants import *
from window import Window
from maze import Maze


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    sleep(0.2)
    while window._running:
        maze = Maze(MAZE_X, MAZE_Y, MAZE_COLUMNS, MAZE_ROWS, 50, window)
        maze.solve()
        if window._running:
            sleep(RESTART_DELAY)
        window._canvas.delete("all")
    window.wait_for_close()


if __name__ == "__main__":
    main()