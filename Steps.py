from graphics import *
import random
import math
n = int(input("how many steps?"))
n2 = int(input("how many times?"))
win = GraphWin("THE GRAPH", 600, 600, False)
scale = math.sqrt(n)
win.setCoords(-(1 + scale), -(1 + scale), 1 + scale, 1 + scale)
points = []
walks = []
def walk(n):
    point = Point(0,0)
    point.setFill("red")
    for i in range(n):
        m = random.randint(1,4)
        p = Point(0,0)
        match m:
            case 1:
                p = Point(0,-1)
            case 2:
                p = Point(-1,0)
            case 3:
                p = Point(0,1)
            case 4:
                p = Point(1,0)
        newPoint = Point(point.x + p.x,  point.y+p.y)
        l = Line(point, newPoint)
        l.setFill("white")
        l.draw(win)
        newPoint.setFill("red")
        newPoint.draw(win)
        points.append(newPoint)
        points.append(l)
        point = newPoint
    update()
    return math.sqrt((point.x)**2 + (point.y)**2)
for i in range(n2):
    walks.append(walk(n))
    for p in points:
        p.undraw()
print("Average: " + str(sum(walks)/len(walks)))
print("Expected: "+ str(math.sqrt(n*math.pi)/2))

