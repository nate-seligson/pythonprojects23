import random
import math
from graphics import *
from time import *

win = GraphWin("THE GRAPH", 800,800, False)
bottom = 100
right = 100
win.setCoords(0,bottom,right,0)
movers = []
w = 4
class Slice:
    def __init__(self, p):
        self.obj = Rectangle(p, Point(p.x + w, p.y + w))
        self.obj.setFill("green")
        self.obj.draw(win)
    
length = 3
snake = []
for y in range(math.floor(bottom/w)):
    for x in range(math.floor(right/w)):
        p = Point(w * x, w * y)
        s = Rectangle(p, Point(p.x + w, p.y + w))
        s.draw(win)
for i in range(length):
    s = Slice(Point(32 - (w * i), 32))
    snake.append(s)
update()
a = None
def Apple():
    global a
    if a != None:
        a.undraw()
    p = Point((4 * random.randint(0,math.floor((right-1)/4))) + 2, (4 * random.randint(0,math.floor((bottom-2)/4))) + 2)
    a = Circle(p, 2)
    a.setFill("red")
    a.draw(win)
def start():
    x = 1
    y = 0
    while True:
        global a
        key = win.checkKey()
        if key != None:
            if key == "w" and y == 0:
                y = -1
                x = 0
            if key == "s" and y == 0:
                y = 1
                x = 0
            if key == "a" and x == 0:
                y = 0
                x = -1
            if key == "d" and x == 0:
                y = 0
                x = 1
        snake[-1].obj.undraw()
        p = Point(snake[0].obj.p1.x + (w * x), snake[0].obj.p1.y + (w * y))
        if p.x == a.getCenter().x-2 and p.y == a.getCenter().y-2:
                 Apple()
        else:
            snake.remove(snake[-1])
        if 0 <= p.x <= right and 0 <= p.y <= bottom:
            for s in snake:
                if s.obj.getP1().x == p.x and s.obj.getP1().y == p.y:
                    end()
                    return
            snake.insert(0,Slice(p))
            sleep(0.1)
        else:
            end()
            return
def end():
    t = Text(Point(50,50), "DEAD")
    t.setSize(30)
    t.draw(win)
    sleep(0.1)
    update()
Apple()
start()
