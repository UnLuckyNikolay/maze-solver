from time import sleep

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAZE_COLUMNS, MAZE_ROWS, RESTART_DELAY
from window import Window
from maze import Maze


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    while window._running:
        maze = Maze(50, 50, MAZE_COLUMNS, MAZE_ROWS, 50, window)
        maze.solve()
        if window._running:
            sleep(RESTART_DELAY)
        window._canvas.delete("all")
    window.wait_for_close()


if __name__ == "__main__":
    main()