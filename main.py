from window import Window, Line, Point
from maze import Cell


def main():
    window = Window(800, 600)
    cell1 = Cell(window)
    cell2 = Cell(window)
    cell3 = Cell(window)
    cell4 = Cell(window)
    cell5 = Cell(window)
    cell1.draw(100, 100, 50)
    cell2.draw(150, 100, 50)
    cell3.draw(100, 150, 50)
    cell4.draw(700, 150, 50)
    cell5.draw(100, 500, 50)
    cell1.draw_path_to(cell2)
    cell2.draw_path_to(cell3)
    cell3.draw_path_to(cell4)
    cell4.draw_path_to(cell5)
    cell4.draw_path_to(cell1)

    window.wait_for_close()


if __name__ == "__main__":
    main()