from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze
def main():
     win = Window(1024, 1024)
     maze = Maze(5, 5, 25, 25, 10, 10, window=win)
     maze.solve()
     win.wait_for_close()

     
main()