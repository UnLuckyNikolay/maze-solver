from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MAZE_COLUMNS, MAZE_ROWS
from window import Window, Line, Point
from maze import Cell, Maze


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    maze = Maze(50, 50, MAZE_COLUMNS, MAZE_ROWS, 50, window)

    window.wait_for_close()


if __name__ == "__main__":
    main()