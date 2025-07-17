from window import Window, Line, Point
from maze import Cell


def main():
    window = Window(800, 600)
    cell1 = Cell(window)
    cell2 = Cell(window)
    cell3 = Cell(window)
    cell1.draw(100, 100, 50)
    cell2.draw(150, 100, 50)
    cell3.draw(100, 150, 50)
    window.wait_for_close()


if __name__ == "__main__":
    main()