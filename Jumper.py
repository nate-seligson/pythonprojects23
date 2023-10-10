import random
import math
from graphics import *
from time import *
win = GraphWin("THE GRAPH", 800,400, False)
bottom = 100
right = 200
w = 6
win.setCoords(0,bottom,right,0)
i = 0
gravScale = 0.5
jump = False
dead = False
for y in range(math.floor(bottom/w)):
    for x in range(math.floor(right/w)):
        p = Point(w * x, w * y)
        s = Rectangle(p, Point(p.x + w, p.y + w))
        s.draw(win)
def isTouching(a, b):
    if a.obj.p1.x <= b.obj.p1.x <= a.obj.p2.x and a.obj.p1.y <= b.obj.p1.y <= a.obj.p2.y:
        return True
    return False
def Translate(obj, x, y):
    obj.p1.x += (x * w)
    obj.p2.x = obj.p1.x + w
    obj.p1.y += (y * w)
    obj.p2.y = obj.p1.y + w
    obj.undraw()
    obj.draw(win)
def setPos(obj, x, y):
    obj.p1.x = x
    obj.p2.x = x + w
    obj.p1.y = y
    obj.p2.y = y + w
    obj.undraw()
    obj.draw(win)
class Player:
    def __init__(self, p):
        self.obj = Rectangle(p, Point(p.x + w, p.y + w))
        self.obj.setFill("white")
        self.obj.draw(win)
class Obstacle:
    def __init__(self):
        self.obj = Rectangle(Point(right, 90), Point(right + w, 90 + w))
        self.obj.setFill("red")
        self.obj.draw(win)
    def reset(self):
        setPos(self.obj, right + (random.randint(0,50) * w), 90)
    def move(self):
        Translate(self.obj, -1, 0)
        if self.obj.p1.x < 0:
            self.reset()
x = Player(Point(12,12))
y = []
for i in range(6):
    y.append(Obstacle())
update()
def Obs():
    for q in y:
        q.move()
def end():
    global dead
    for i in y:
        i.obj.undraw()
        y.remove(i)
        x.obj.undraw()
        t = Text(Point(100,50),"You Died!")
        t.setSize(30)
        t.draw(win)
        update()
        dead = True
while not dead:
    k = win.checkKey()
    if k != None:
        if k == "space":
            jumpForce = 0
            while jumpForce < 2:
                jump = True
                Translate(x.obj, 0, -2 + round(jumpForce))
                update()
                jumpForce += gravScale
                Obs()
                sleep(0.1)
            jump = False
            jumpForce = 0
    if x.obj.p1.y < 90 and not jump:
        while x.obj.p1.y < 90:
            Translate(x.obj, 0, round(i))
            if x.obj.p1.y > 90:
                setPos(x.obj, x.obj.p1.x, 90)
            update()
            Obs()
            sleep(0.1)
            i+=gravScale
        i = 0
    for a in y:
        if isTouching(a, x):
            end()
    else:
        Obs()
        sleep(0.1)
    
