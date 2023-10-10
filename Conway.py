from graphics import *
import math
import random
import time
from threading import Thread
win = GraphWin("THE GRAPH", 800,800, False)
bottom = 100
right = 100
win.setCoords(0,bottom,right,0)
w = int(input("box width?"))
squares = []
class Square:
    def __init__(self, point, x,y):
        self.obj = Rectangle(point,Point(point.x + w,point.y + w))
        self.obj.setFill("Gray")
        self.amt = 0
        self.alive = False
        self.needsFlip = False
        self.coords = [x,y]
    def findMines(self):
            x = self.coords[0]
            y = self.coords[1]
            self.amt = 0
            for i in squares:
                cx = i.coords[0]
                cy = i.coords[1]
                xdis=abs(x - cx)
                ydis=abs(y-cy)
                if xdis<2 and ydis<2 and 0 < xdis+ydis <= 2 and i.alive:
                  self.amt += 1
    def flip(self):
        self.alive = not self.alive
        if self.alive:
            self.obj.setFill("White")
            
        else:
            self.obj.setFill("Gray")
def GodsPlan(s):
        if s.alive:
            if s.amt < 2:
                return True
            elif s.amt >= 4:
                return True
        else:
            if s.amt == 3:
                return True
        return False
        
for y in range(math.floor(bottom/w)):
    for x in range(math.floor(right/w)):
        p = Point(w * x, w * y)
        s = Square(p,x,y)
        s.obj.draw(win)
        squares.append(s)
for s in squares:
    s.findMines()
update()
def Main():
    while True:
        k = win.checkKey()
        click = win.checkMouse()
        if k == "space":
            while win.checkKey() != "space":
                for s in squares:
                    s.findMines()
                    s.needsFlip = GodsPlan(s)
                for s in squares:
                    if s.needsFlip:
                        s.flip()
                update()
        if click != None:
            for i in squares:
                if i.obj.getP1().x < click.x < i.obj.getP2().x and i.obj.getP1().y < click.y < i.obj.getP2().y:
                    i.flip()
m = Thread(target = Main, daemon = True)
m.run()
