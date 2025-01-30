from point import Point
from cell import Cell
import time
import random
class Maze():
     def __init__(self,x1,y1,numRows,numCols,cellSizeX,cellSizeY,window = None, seed = None):
          self.x1 = x1
          self.y1 = y1
          self.numRows = numRows
          self.numCols = numCols
          self.cellSizeX = cellSizeX
          self.cellSizeY = cellSizeY
          self.win = window
          self.cells = []
          if seed:
               random.seed(seed)
          self.createCells()
     def createCells(self):
          for i in range(0,self.numCols):
               y = self.y1 + (self.cellSizeY * i)
               self.cells.append([])
               for j in range(0,self.numRows):
                    x = self.x1 + (self.cellSizeX * j)
                    p1 = Point(x,y)
                    p2 = Point(x+self.cellSizeX,y+self.cellSizeY)
                    self.cells[i].append(Cell(p1,p2,self.win))
          self.updateCells()
          self.breakEntranceExit()
          self.breakWallsRecursive(0,0)
          self.resetCellsVisited()
     def updateCells(self):
          for c in self.cells:
               for cell in c:
                    cell.draw()
                    self.animate()
     def animate(self):
          if self.win:
               self.win.redraw()
               time.sleep(0.05)
     def breakEntranceExit(self):
          entranceCell = self.cells[0][0]
          exitCell = self.cells[self.numCols-1][self.numRows-1]
          north = random.randint(0,1) == 1
          east = random.randint(0,1) == 1
          if north:
               entranceCell.n = False
               entranceCell.draw()
          else:
               entranceCell.w = False
               entranceCell.draw()
          if east:
               exitCell.e = False
               exitCell.draw()
          else:
               exitCell.s = False
               exitCell.draw()
     def breakWallsRecursive(self,i,j):
          self.cells[i][j].visited = True
          while True:
               to_visit = []
               #find unvisited neighbors
               if i > 0:
                    northNeighbor = self.cells[i-1][j]
                    if not northNeighbor.visited:
                         to_visit.append((i-1,j))
               if j+1 != self.numRows:
                    eastNeighbor = self.cells[i][j+1]
                    if not eastNeighbor.visited:
                         to_visit.append((i,j+1))
               if i+1 != self.numCols:
                    southNeighbor = self.cells[i+1][j]
                    if not southNeighbor.visited:
                         to_visit.append((i+1,j))
               if j > 0:
                    westNeighbor = self.cells[i][j-1]
                    if not westNeighbor.visited:
                         to_visit.append((i,j-1))
               
               # break out of loop if there are no unvisited neighbors
               if not to_visit:
                    self.cells[i][j].draw()
                    return
               #choose random neighbor
               nextCoords = to_visit[random.randint(0,len(to_visit)-1)]
               
               difI = i - nextCoords[0]
               difJ = j - nextCoords[1]
               #break walls between neighbor and current cell
               if difI == -1:
                    self.cells[i][j].s = False
                    self.cells[i][j].draw()
                    self.cells[i+1][j].n = False
                    self.cells[i+1][j].draw()
               elif difI == 1:
                    self.cells[i][j].n = False
                    self.cells[i][j].draw()
                    self.cells[i-1][j].s = False
                    self.cells[i-1][j].draw()
               elif difJ == -1:
                    self.cells[i][j].e = False
                    self.cells[i][j].draw()  
                    self.cells[i][j+1].w = False
                    self.cells[i][j+1].draw()
               elif difJ == 1:
                    self.cells[i][j].w = False
                    self.cells[i][j].draw()
                    self.cells[i][j-1].e = False
                    self.cells[i][j-1].draw()  
               #move to next cell
               self.breakWallsRecursive(nextCoords[0],nextCoords[1])

     def resetCellsVisited(self):
          for c in self.cells:
               for cell in c:
                    cell.visited = False

     def solve(self):
          return self.solve_r(0,0)
     def solve_r(self,i,j):
          self.animate()
          self.cells[i][j].visited = True
          if i == self.numCols - 1 and j == self.numRows - 1:
               return True
          if i > 0:
               northNeighbor = self.cells[i-1][j]
               if not northNeighbor.visited and not northNeighbor.s and not self.cells[i][j].n:
                    self.cells[i][j].drawMove(northNeighbor)
                    res = self.solve_r(i-1,j)
                    if res:
                         return res
                    else:
                         self.cells[i][j].drawMove(northNeighbor,undo=True)
                    
          if j+1 != self.numRows:
               eastNeighbor = self.cells[i][j+1]
               if not eastNeighbor.visited and not eastNeighbor.w and not self.cells[i][j].e:
                    self.cells[i][j].drawMove(eastNeighbor)
                    res = self.solve_r(i,j+1)
                    if res:
                         return res
                    else:
                         self.cells[i][j].drawMove(eastNeighbor,undo=True)
          if i+1 != self.numCols:
               southNeighbor = self.cells[i+1][j]
               if not southNeighbor.visited and not southNeighbor.n and not self.cells[i][j].s:
                    self.cells[i][j].drawMove(southNeighbor)
                    res = self.solve_r(i+1,j)
                    if res:
                         return res
                    else:
                         self.cells[i][j].drawMove(southNeighbor,undo=True)
          if j > 0:
               westNeighbor = self.cells[i][j-1]
               if not westNeighbor.visited and not westNeighbor.e and not self.cells[i][j].w:
                    self.cells[i][j].drawMove(westNeighbor)
                    res = self.solve_r(i,j-1)
                    if res:
                         return res
                    else:
                         self.cells[i][j].drawMove(westNeighbor,undo=True)
          return False

     def __repr__(self) -> str:
          cells = []
          for i in range(0,len(self.cells)):
               cells.append([])
               for cell in self.cells[i]:
                    cells[i].append(cell.__repr__())
          return cells.__str__()
                    
