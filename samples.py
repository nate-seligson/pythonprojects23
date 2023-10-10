from graphics import *
from random import *
import math
inp = int(input("How many samples would you like to run?"))
win = GraphWin("THE GRAPH", 800, 600, autoflush = False)
win.setBackground("white")
win.setCoords(0,0,4,3)
rect = Rectangle(Point(1.5,1),Point(2.5,2))
rect.draw(win)
distances = []
for i in range(inp):
    points = []
    for i in range(2):
      p = Point(1.5 + random(), 1+random())
      p.draw(win)
      points.append(p)
    l = Line(points[0], points[1])
    l.draw(win)
    distance = math.sqrt((points[0].getX() - points[1].getX())**2+(points[0].getY()-points[1].getY())**2)
    distances.append(distance)
print(sum(distances)/len(distances))
update()
    

    
      

