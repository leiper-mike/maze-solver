import unittest
from maze import Maze

class MazeTests(unittest.TestCase):
     def test_maze_create_cells(self):
          num_cols = 12
          num_rows = 10
          m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
          self.assertEqual(
               len(m1.cells),
               num_cols,
          )
          self.assertEqual(
               len(m1.cells[0]),
               num_rows,
          )
     def test_maze_create_cells_square(self):
          num_cols = 10
          num_rows = 10
          m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
          self.assertEqual(
               len(m1.cells),
               num_cols,
          )
          self.assertEqual(
               len(m1.cells[0]),
               num_rows,
          )
     def test_maze_create_cells_shallow(self):
          num_cols = 12
          num_rows = 1
          m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
          self.assertEqual(
               len(m1.cells),
               num_cols,
          )
          self.assertEqual(
               len(m1.cells[0]),
               num_rows,
          )
     def test_maze_create_cells_deep(self):
          num_cols = 1
          num_rows = 10
          m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
          self.assertEqual(
               len(m1.cells),
               num_cols,
          )
          self.assertEqual(
               len(m1.cells[0]),
               num_rows,
          )
     def test_maze_break_entrance_exit(self):
          num_cols = 10
          num_rows = 10
          m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
          entrance = m1.cells[0][0]
          exitCell = m1.cells[num_cols-1][num_rows-1]
          
          self.assertEqual(entrance.n ^ entrance.w,True)
          self.assertEqual(exitCell.e ^ exitCell.s,True) 
     def test_maze_break_walls(self):
          m1 = Maze(0, 0, 10, 10, 10, 10, seed=0)
          broken = True
          for c in m1.cells:
               for cell in c:
                    broken = not (cell.n and cell.s and cell.e and cell.w)
                    if not broken:
                         break 
               if not broken:
                         break 
          self.assertEqual(broken, True)
     def test_maze_reset_visited(self):
          m1 = Maze(0, 0, 10, 10, 10, 10, seed=0)
          m1.breakWallsRecursive(0,0)
          visited = True
          for c in m1.cells:
               for cell in c:
                    visited = cell.visited
                    if not visited:
                         break 
               if not visited:
                         break 
          self.assertEqual(visited, True)
if __name__ == "__main__":
    unittest.main()