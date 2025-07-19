import unittest

from maze import Maze


class TestMaze(unittest.TestCase):
    def setUp(self):
        self.num_cols = 12
        self.num_rows = 10
        self.maze = Maze(50, 50, self.num_cols, self.num_rows, 50)
        
        
    def test__maze__create_cells(self):
        self.assertEqual(
            len(self.maze._cells),
            self.num_cols
        )
        self.assertEqual(
            len(self.maze._cells[0]),
            self.num_rows
        )

    def test__maze__exit_and_entrance(self):
        self.assertEqual(
            self.maze._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            self.maze._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall,
            False
        )

    def test__cell__coords(self):
        self.assertEqual(
            self.maze._cells[5][0]._x1,
            300
        )
        self.assertEqual(
            self.maze._cells[5][0]._y1,
            50
        )

        self.assertEqual(
            self.maze._cells[2][3]._x1,
            150
        )
        self.assertEqual(
            self.maze._cells[2][3]._y1,
            200
        )
        self.assertEqual(
            self.maze._cells[2][3]._x2,
            200
        )
        self.assertEqual(
            self.maze._cells[2][3]._y2,
            250
        )


if __name__ == "__main__":
    unittest.main()