from window import Window, Line, Point
from maze import Cell, Maze


def main():
    window = Window(800, 600)
    maze = Maze(50, 50, 14, 10, 50, window)

    window.wait_for_close()


if __name__ == "__main__":
    main()