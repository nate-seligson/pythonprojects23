from graphics import *
import math
import random
win = GraphWin("THE GRAPH", 800,800, False)
w = 3#int(input("box width?"))
bombs =150#int(input("how many bombs?(max is " + str(int(math.floor((bottom * right)/(w**2)))) + ")" ))
squares = []
instance = 0
def Lose():
    global instance
    Run()
def flip(m):
    global mode
    global flagm
    if m:
        mode = "on"
    else:
        mode = "off"
    flagm.undraw()
    flagm = Text(Point(90,90), "Flag mode:" + mode)
    flagm.setSize(20)
    flagm.draw(win)
    update()
class Square:
    def __init__(self, point):
        self.obj = Rectangle(point,Point(point.x + w,point.y + w))
        self.hasMine = False
        self.num = 0
        self.l = []
        self.revealed = False
        self.flagged = False
        self.c = ""
    def attatchNum(self):
        t = Text(self.obj.getCenter(), str(self.num))
        t.draw(win)
    def reveal(self):
        if not self.hasMine:
            self.obj.setFill("white")
        else:
            self.obj.setFill("red")
            Lose()
            return
        if self.num > 0:
               self.attatchNum()
        self.revealed = True
        for i in self.l:
            if i.num == 0 and not i.hasMine and not i.revealed:
                i.reveal()
            elif self.num == 0 and i.num > 0 and not i.revealed:
                i.reveal()
                i.attatchNum()
    def findMines(self):
            for i in squares:
                if (abs(i.obj.getP1().x-self.obj.getP1().x) == w or abs(i.obj.getP1().y-self.obj.getP1().y) == w) and abs(i.obj.getP1().x-self.obj.getP1().x) + abs(i.obj.getP1().y-self.obj.getP1().y) <= w*2:
                  self.l.append(i)
                  if i.hasMine:
                        self.num += 1
    def flag(self):
        if not self.flagged:
            self.c = Circle(self.obj.getCenter(), w/2)
            self.c.setFill("red")
            self.c.draw(win)
            self.flagged = True
        else:
            self.c.undraw()
            self.flagged = False
def Run():
    global squares
    global bombs
    global win
    global instance
    squares = []
    try:
        for item in win.items[:]:
            item.undraw()
        update()
    except:
        pass
    bottom = 100
    right = 100
    win.setCoords(0,bottom,right,0)
    mode = "off"
    flagm = Text(Point(90,90), "Flag mode:" + mode)
    flagm.setSize(20)
    for y in range(math.floor(bottom/w)):
        for x in range(math.floor(right/w)):
            p = Point(w * x, w * y)
            s = Square(p)
            s.obj.draw(win)
            squares.append(s)
    for i in range(bombs):
        nonos = []
        r = random.randint(0,len(squares)-1)
        while nonos.count(r) != 0:
            r = random.randint(0,len(squares))
        nonos.append(r)
        squares[r].hasMine = True
    for i in squares:
        i.findMines()
    update()
    flagMode = False
    while True:
        x = squares[random.randrange(0,len(squares)-1)]
        if not x.hasMine:
            x.reveal()
            update()
            break
    return squares
def Start():
    while True:
        click = win.checkMouse()
        key = win.checkKey()
        if key == "f":
            flagMode = not flagMode
            flip(flagMode)
        if click != None:
            for i in squares:
                if i.obj.getP1().x < click.x < i.obj.getP2().x and i.obj.getP1().y < click.y < i.obj.getP2().y:
                    if not flagMode and not i.flagged:
                        i.reveal()
                    elif not i.revealed:
                        i.flag()

