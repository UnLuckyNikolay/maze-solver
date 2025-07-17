from window import Window, Line, Point


def main():
    window = Window(800, 600)
    line1 = Line(Point(100, 100), Point(200, 200))
    line2 = Line(Point(150, 200), Point(200, 200))
    line3 = Line(Point(150, 200), Point(300, 150))
    window.draw_line(line1, "black")
    window.draw_line(line2, "gray")
    window.draw_line(line3, "red")
    window.wait_for_close()


if __name__ == "__main__":
    main()