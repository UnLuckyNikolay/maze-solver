from __future__ import annotations

from time import sleep
from enum import Enum
import random

from constants import *
from window import Window, Line, Point


class CellWall(Enum):
    RIGHT = "right"
    BOTTOM = "bottom"
    LEFT = "left"
    TOP = "top"

class WallType(Enum):
    CORNER = "corner"
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"    
    

class Maze:
    def __init__(self, x1 : int, y1 : int, num_cols : int, num_rows : int, cell_size : int, window : Window | None = None, seed : int | None = None):
        self._window = window
        self._x1 = x1
        self._y1 = y1
        self._num_cols = num_cols
        self._num_rows = num_rows
        self._cell_size = cell_size
        self._cells : list[list[Cell]] = []

        if MAZE_SEED_OVERRIDE:
            random.seed(MAZE_SEED)
        else:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls()


    def _create_cells(self):
        for x in range(self._num_cols):
            self._cells.append([])
            for y in range(self._num_rows):
                self._cells[x].append(
                    Cell(
                        x, y, 
                        self._x1 + x * self._cell_size, self._y1 + y * self._cell_size,
                        self._window
                    )
                )
                self._draw_cell(x, y, ANIMATION_DELAY_BUILD)

    def _draw_cell(self, x : int, y : int, delay : float):
        self._cells[x][y].redraw()
        self._animate(delay)

    def _animate(self, delay : float):
        if self._window == None:
            return
        if self._window._running == False:
            return
        
        self._window.redraw()
        sleep(delay)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0, ANIMATION_DELAY_BREAK)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1, ANIMATION_DELAY_BREAK)

    def _break_walls(self):
        self._cells[self._num_cols-1][self._num_rows-1]._broken_in = True
        self._draw_cell(self._num_cols-1, self._num_rows-1, ANIMATION_DELAY_BREAK)
        self._break_walls_i_r(self._num_cols-1, self._num_rows-1)

    def _break_walls_i_r(self, x : int, y : int):
        possible_dir : list[tuple[int, int]] = []
        current_cell = self._cells[x][y]

        if x > 0 and self._cells[x-1][y]._broken_in == False:
            possible_dir.append((x-1, y))
        if y > 0 and self._cells[x][y-1]._broken_in == False:
            possible_dir.append((x, y-1))
        if x < self._num_cols-1 and self._cells[x+1][y]._broken_in == False:
            possible_dir.append((x+1, y))
        if y < self._num_rows-1 and self._cells[x][y+1]._broken_in == False:
            possible_dir.append((x, y+1))

        while len(possible_dir) > 0:
            for x_, y_ in reversed(possible_dir):
                if self._cells[x_][y_]._broken_in == True:
                    possible_dir.remove((x_, y_))
            
            if len(possible_dir) == 0:
                return

            next_xy = random.choice(possible_dir)
            nx = next_xy[0]
            ny = next_xy[1]
            next_cell : Cell = self._cells[nx][ny]
            possible_dir.remove(next_xy)

            if current_cell._x1 < next_cell._x1:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif current_cell._x1 > next_cell._x1:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif current_cell._y1 < next_cell._y1:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            else:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            
            next_cell._broken_in = True
            self._draw_cell(nx, ny, ANIMATION_DELAY_BREAK)

            self._break_walls_i_r(nx, ny)

    def solve(self) -> bool:     
        if self._window != None:
            self._window.draw_line(
                Line(
                    Point(self._cells[0][0]._x_center, self._cells[0][0]._y_center - self._cell_size), 
                    Point(self._cells[0][0]._x_center, self._cells[0][0]._y_center)
                ), COLOR_PATH_CURRENT
            )
        return self._solve_i_r(0, 0)

    def _solve_i_r(self, x : int, y : int) -> bool:
        if self._window != None and self._window._running == False:
            return False
        
        current_cell = self._cells[x][y]
        current_cell._visited = True
        
        self._animate(ANIMATION_DELAY_DRAW)
        if x == self._num_cols-1 and y == self._num_rows-1:
            if self._window != None:
                self._window.draw_line(
                    Line(
                        Point(current_cell._x_center, current_cell._y_center), 
                        Point(current_cell._x_center, current_cell._y_center + self._cell_size)
                    ), COLOR_PATH_CURRENT
                )
            return True

        # Pathing checks
        # Right
        if (
            not current_cell.has_right_wall 
            and self._cells[x+1][y]._visited == False
        ):
            current_cell.draw_path_to(self._cells[x+1][y])
            right = self._solve_i_r(x+1, y)
            if right:
                return True
            else: 
                current_cell.draw_path_to(self._cells[x+1][y], True)
                self._animate(ANIMATION_DELAY_UNDO)
        else:
            right = False

        # Bottom
        if (
            not current_cell.has_bottom_wall
            and self._cells[x][y+1]._visited == False
        ):
            current_cell.draw_path_to(self._cells[x][y+1])
            bottom = self._solve_i_r(x, y+1)
            if bottom:
                return True
            else: 
                current_cell.draw_path_to(self._cells[x][y+1], True)
                self._animate(ANIMATION_DELAY_UNDO)
        else:
            bottom = False

        # Left
        if (
            not current_cell.has_left_wall
            and self._cells[x-1][y]._visited == False
        ):
            if (
                y == 0
                or y == self._num_rows - 1
            ):
                left = False
                if DEBUG_CHECK_DEAD_END:
                    current_cell.draw_cross(CellWall.LEFT)
                    self._animate(ANIMATION_DELAY_UNDO)
            else:
                current_cell.draw_path_to(self._cells[x-1][y])
                left = self._solve_i_r(x-1, y)
                if left:
                    return True
                else: 
                    current_cell.draw_path_to(self._cells[x-1][y], True)
                    self._animate(ANIMATION_DELAY_UNDO)
        else:
            left = False

        # Top
        if (
            not current_cell.has_top_wall
            and self._cells[x][y-1]._visited == False
        ):
            if (
                x == 0 
                or x == self._num_cols - 1
            ):
                top = False
                if DEBUG_CHECK_DEAD_END:
                    current_cell.draw_cross(CellWall.TOP)
                    self._animate(ANIMATION_DELAY_UNDO)
            else:
                current_cell.draw_path_to(self._cells[x][y-1])
                top = self._solve_i_r(x, y-1)
                if top:
                    return True
                else: 
                    current_cell.draw_path_to(self._cells[x][y-1], True)
                    self._animate(ANIMATION_DELAY_UNDO)
        else:
            top = False

        return right or bottom or left or top


class Cell:
    def __init__(self, x_grid, y_grid, x1, y1, window : Window | None = None):
        self._x1 = x1
        self._x2 = x1 + CELL_SIZE
        self._x_center = int((self._x1 + self._x2) / 2)
        self._x_grid = x_grid
        self._y1 = y1
        self._y2 = y1 + CELL_SIZE
        self._y_center = int((self._y1 + self._y2) / 2)
        self._y_grid = y_grid
        self._window = window
        self._broken_in = False
        self._visited = False
        
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

        self.corner_tl = None
        self.corner_tr = None
        self.corner_bl = None
        self.corner_br = None

        self._wall_t = None
        self._wall_r = None
        self._wall_b = None
        self._wall_l = None
    
    def redraw(self):
        if self._window == None:
            return

        # Corners
        #self.draw_corner(Point(self._x1, self._y1))
        #self.draw_corner(Point(self._x1, self._y2))
        #self.draw_corner(Point(self._x2, self._y2))
        #self.draw_corner(Point(self._x2, self._y1))
        self.corner_tl = Wall(self._x1, self._y1, WallType.CORNER, self._window)
        self.corner_tr = Wall(self._x2, self._y1, WallType.CORNER, self._window)
        self.corner_bl = Wall(self._x1, self._y2, WallType.CORNER, self._window)
        self.corner_br = Wall(self._x2, self._y2, WallType.CORNER, self._window)

        # Walls
        if self.has_top_wall:
            self.draw_wall(Point(self._x1, self._y1), Point(self._x2, self._y1), COLOR_WALL_TOP)
        else:
            self.draw_wall(Point(self._x1, self._y1), Point(self._x2, self._y1), COLOR_BACKGROUND)

        if self.has_right_wall:
            self.draw_wall(Point(self._x2, self._y1), Point(self._x2, self._y2), COLOR_WALL_TOP)
        else:
            self.draw_wall(Point(self._x2, self._y1), Point(self._x2, self._y2), COLOR_BACKGROUND)

        if self.has_bottom_wall:
            self.draw_wall(Point(self._x2, self._y2), Point(self._x1, self._y2), COLOR_WALL_TOP)
        else:
            self.draw_wall(Point(self._x2, self._y2), Point(self._x1, self._y2), COLOR_BACKGROUND)

        if self.has_left_wall:
            self.draw_wall(Point(self._x1, self._y2), Point(self._x1, self._y1), COLOR_WALL_TOP)
        else:
            self.draw_wall(Point(self._x1, self._y2), Point(self._x1, self._y1), COLOR_BACKGROUND)

        # Debug check marks for broken in cells
        if DEBUG_CHECK_BROKEN_IN_CELL and self._broken_in:
            self._window.draw_line(Line(Point(self._x1+5, self._y1+5), Point(self._x1+10, self._y1+10)), DEBUG_CHECK_BROKEN_IN_COLOR)
            self._window.draw_line(Line(Point(self._x1+10, self._y1+10), Point(self._x1+15, self._y1+5)), DEBUG_CHECK_BROKEN_IN_COLOR)

    def draw_wall(self, point1 : Point, point2 : Point, color : str):
        if self._window == None:
            return
        
        corner = int(WIDTH_CORNER / 2)
        wall = int(WIDTH_WALL / 2)

        if point1.x == point2.x:
            if point1.y < point2.y:
                self._window.draw_line(Line(Point(point1.x + wall, point1.y + corner), Point(point2.x + wall, point2.y - corner)), color)
                self._window.draw_line(Line(Point(point1.x - wall, point1.y + corner), Point(point2.x - wall, point2.y - corner)), color)
            if point1.y > point2.y:
                self._window.draw_line(Line(Point(point1.x + wall, point1.y - corner), Point(point2.x + wall, point2.y + corner)), color)
                self._window.draw_line(Line(Point(point1.x - wall, point1.y - corner), Point(point2.x - wall, point2.y + corner)), color)
        elif point1.y == point2.y:
            if point1.x < point2.x:
                self._window.draw_line(Line(Point(point1.x + corner, point1.y - wall), Point(point2.x - corner, point2.y - wall)), color)
                self._window.draw_line(Line(Point(point1.x + corner, point1.y + wall), Point(point2.x - corner, point2.y + wall)), color)
            if point1.x > point2.x:
                self._window.draw_line(Line(Point(point1.x - corner, point1.y - wall), Point(point2.x + corner, point2.y - wall)), color)
                self._window.draw_line(Line(Point(point1.x - corner, point1.y + wall), Point(point2.x + corner, point2.y + wall)), color)
    
    def draw_corner(self, point : Point):
        if self._window == None:
            return
        
        dist = int(WIDTH_CORNER / 2)
        self._window.draw_line(Line(Point(point.x - dist, point.y - dist), Point(point.x + dist, point.y - dist)), COLOR_WALL_TOP)
        self._window.draw_line(Line(Point(point.x + dist, point.y - dist), Point(point.x + dist, point.y + dist)), COLOR_WALL_TOP)
        self._window.draw_line(Line(Point(point.x + dist, point.y + dist), Point(point.x - dist, point.y + dist)), COLOR_WALL_TOP)
        self._window.draw_line(Line(Point(point.x - dist, point.y + dist), Point(point.x - dist, point.y - dist)), COLOR_WALL_TOP)

    def draw_cross(self, wall : CellWall):
        if self._window == None:
            return
        
        match (wall):
            case CellWall.RIGHT:
                x = self._x2
                y = self._y_center
            case CellWall.BOTTOM:
                x = self._x_center
                y = self._y2
            case CellWall.LEFT:
                x = self._x1
                y = self._y_center
            case CellWall.TOP:
                x = self._x_center
                y = self._y1
        
        size_half = 5
        self._window.draw_line(Line(Point(x - size_half, y - size_half), Point(x + size_half, y + size_half)), DEBUG_CHECK_DEAD_END_COLOR)
        self._window.draw_line(Line(Point(x + size_half, y - size_half), Point(x - size_half, y + size_half)), DEBUG_CHECK_DEAD_END_COLOR)        

    def draw_path_to(self, to_cell : Cell, undo : bool = False):
        if self._window == None:
            return
        
        color = COLOR_PATH_CURRENT if not undo else COLOR_PATH_UNDO

        self._window.draw_line(Line(
            Point(self._x_center, self._y_center), 
            Point(to_cell._x_center, to_cell._y_center)
        ), fill_color=color)


class Wall:
    def __init__(self, x : int, y : int, type : WallType, window : Window):
        self._window = window

        match (type):
            case WallType.CORNER:
                self._light = self._window._canvas.create_polygon(
                    (int(x - WIDTH_CORNER / 2 - HEIGHT_WALL), int(y + WIDTH_CORNER / 2 - HEIGHT_WALL)),
                    (int(x + WIDTH_CORNER / 2 - HEIGHT_WALL), int(y + WIDTH_CORNER / 2 - HEIGHT_WALL)),
                    (int(x + WIDTH_CORNER / 2), int(y + WIDTH_CORNER / 2)),
                    (int(x - WIDTH_CORNER / 2), int(y + WIDTH_CORNER / 2)),
                    outline=COLOR_WALL_LIGHT,
                    width=WIDTH_LINE,
                    fill=COLOR_WALL_LIGHT_FILL
                )
                self._dark = self._window._canvas.create_polygon(
                    (int(x + WIDTH_CORNER / 2 - HEIGHT_WALL), int(y - WIDTH_CORNER / 2 - HEIGHT_WALL)),
                    (int(x + WIDTH_CORNER / 2 - HEIGHT_WALL), int(y + WIDTH_CORNER / 2 - HEIGHT_WALL)),
                    (int(x + WIDTH_CORNER / 2), int(y + WIDTH_CORNER / 2)),
                    (int(x + WIDTH_CORNER / 2), int(y - WIDTH_CORNER / 2)),
                    outline=COLOR_WALL_DARK,
                    width=WIDTH_LINE,
                    fill=COLOR_WALL_DARK_FILL
                )
                self._top = self._window._canvas.create_rectangle(
                    (int(x - WIDTH_CORNER / 2 - HEIGHT_WALL), int(y - WIDTH_CORNER / 2 - HEIGHT_WALL)),
                    (int(x + WIDTH_CORNER / 2 - HEIGHT_WALL), int(y + WIDTH_CORNER / 2 - HEIGHT_WALL)),
                    outline=COLOR_WALL_TOP,
                    width=WIDTH_LINE,
                    fill=COLOR_WALL_TOP_FILL
                )

    def delete(self):
        self._window._canvas.delete(self._top)
        self._window._canvas.delete(self._dark)
        self._window._canvas.delete(self._light)