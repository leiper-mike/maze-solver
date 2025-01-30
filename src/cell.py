from line import Line
from point import Point
class Cell():
     def __init__(self,p1,p2,window = None):
          self.n = True
          self.e = True
          self.s = True
          self.w = True
          self.x1 = p1.x
          self.y1 = p1.y
          self.x2 = p2.x
          self.y2 = p2.y
          self.center = ((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
          self.window = window
          self.visited = False
     def draw(self):
          if self.window:
               if self.n:
                    Line(Point(self.x1,self.y1),Point(self.x2,self.y1)).draw(self.window.canvas,"black")
               else:
                    Line(Point(self.x1,self.y1),Point(self.x2,self.y1)).draw(self.window.canvas,"white")
               if self.e:
                    Line(Point(self.x2,self.y1),Point(self.x2,self.y2)).draw(self.window.canvas,"black")
               else:
                    Line(Point(self.x2,self.y1),Point(self.x2,self.y2)).draw(self.window.canvas,"white")
               if self.s:
                    Line(Point(self.x1,self.y2),Point(self.x2,self.y2)).draw(self.window.canvas,"black")
               else:
                    Line(Point(self.x1,self.y2),Point(self.x2,self.y2)).draw(self.window.canvas,"white")
               if self.w:
                    Line(Point(self.x1,self.y2),Point(self.x1,self.y1)).draw(self.window.canvas,"black")
               else:
                    Line(Point(self.x1,self.y2),Point(self.x1,self.y1)).draw(self.window.canvas,"white")
     def drawMove(self, toCell, undo=False):
          if self.window:
               color = "red"
               if undo:
                    color = "gray"
               Line(Point(self.center[0],self.center[1]),Point(toCell.center[0],toCell.center[1])).draw(self.window.canvas,color)
     def __repr__(self) -> str:
          rep = ""
          if self.w:
               rep+="|"
          if self.n:
               if self.s:
                    rep+="="
               else:
                    rep+="-"
          elif self.s:
               rep+="_"
          if self.e:
               rep+="|"
          return rep