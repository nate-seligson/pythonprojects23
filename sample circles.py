from graphics import *
import random
import math
inp = int(input("How many samples would you like to run?"))
win = GraphWin("THE GRAPH", 800, 600, autoflush = False)
win.setCoords(0,0,4,3)
circle = Circle(Point(2,1.5), 1)
c = circle.getCenter()
circle.draw(win)
i=0
points = []
while i < inp:
  p = Point(2 + random.uniform(-1,1), 1.5 + random.uniform(-1,1))
  if abs(math.sqrt((p.x - c.x)**2 + (p.y - c.y)**2)) < 1:
    p.draw(win)
    points.append(p)
    i+=1
for i in range(len(points)):
  if i % 2 == 0 and i > 0:
    l = Line(points[i], points[i-1])
    l.draw(win)
distances = []
distance = math.sqrt((points[0].getX() - points[1].getX())**2+(points[0].getY()-points[1].getY())**2)
distances.append(distance)
print(sum(distances)/len(distances))
update()
