from graphics import *
import random
import math
b1 = 0;
successes = 0
win = GraphWin("THE GRAPH", 800, 600, autoflush = False)
win.setCoords(-1,-2,2,2)
l = Line(Point(0,0), Point(1,0))
def draw(d1,d2,d3):
    l1 = Line(Point(0,0), Point(d1,0))
    l1.setFill("red")
    l2 = Line(Point(d1,0), Point(d1+d2,0))
    l2.setFill("white")
    l3 = Line(Point(1,0), Point(1-d3,0))
    l3.setFill("blue")
    l1.draw(win)
    l2.draw(win)
    l3.draw(win)
    update()
    l1.undraw()
    l2.undraw()
    l3.undraw()
def breakBigger(b1):
    if b1 > (1-b1) :
        b2 = random.random() * b1
    else:
        b2 = random.uniform(b1,1)
    return b1,b2
def breakSameTime(b1):
    b2 = random.random()
    return b1,b2
def breakRandom(b1):
    r = random.randrange(0,1)
    if r == 1:
        b2 = random.random() * b1
    else:
        b2 = random.uniform(b1,1)
    return b1,b2
def isTriangle(b1, b2):
    global successes
    if b1<b2:
        d1 = b1
        d3 = 1-b2
    else:
        d1 = b2
        d3 = 1-b1
    d2 = abs(b2-b1)
    draw(d1,d2,d3)
    if d1 + d2 >= d3 and d2 + d3 >= d1 and d1+d3>=d2:
        successes += 1
        
n = int(input("how many times to run?"))
for i in range(n):
    b1 = random.random()
    isTriangle(*breakBigger(b1))
print("Formula 1 success rate: " + str(successes) + " / " + str(n) + ", " + str(successes / n))
successes = 0
for i in range(n):
    b1 = random.random()
    isTriangle(*breakSameTime(b1))
print("Formula 2 success rate: " + str(successes) + " / " + str(n) + ", " + str(successes / n))
successes = 0
for i in range(n):
    b1 = random.random()
    isTriangle(*breakRandom(b1))
print("Formula 3 success rate: " + str(successes) + " / " + str(n) + ", " + str(successes / n))
