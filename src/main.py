from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze
def main():
     win = Window(1024, 920)
     maze = Maze(5, 5, 10, 10, 10, 10, window=win)
     maze.solve()
     maze = Maze(200, 200, 10, 10, 10, 10, window=win)
     maze.solve()
     maze = Maze(5, 200, 10, 10, 10, 10, window=win)
     maze.solve()
     maze = Maze(200, 5, 10, 10, 10, 10, window=win)
     maze.solve()
     win.wait_for_close()
main()