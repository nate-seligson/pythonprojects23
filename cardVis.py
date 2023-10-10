from graphics import *
from math import *
import time
win = None
def init(w):
    global win
    win = w
def undrawl(objs):
    for obj in objs:
        obj.undraw()
class heart:
    def __init__(self, pos, scale = 1):
        scale = scale-(0.2 * scale)
        w = 10 * scale
        leftbump = Oval(Point(pos.x-w,pos.y-w), Point(pos.x+w/8, pos.y))
        rightbump = Oval(Point(pos.x+w,pos.y-w), Point(pos.x-w/8, pos.y))
        pointy = Polygon(Point(pos.x - w + 0.2 * scale, pos.y-3 * scale), Point(pos.x + w - 0.2 * scale, pos.y-3 * scale), Point(pos.x, pos.y+w/1.5))
        leftbump.setFill("red")
        rightbump.setFill("red")
        pointy.setFill("red")
        leftbump.setWidth(0)
        rightbump.setWidth(0)
        pointy.setWidth(0)
        pointy.draw(win)
        leftbump.draw(win)
        rightbump.draw(win)
        self.objs = []
        self.objs.append(leftbump)
        self.objs.append(rightbump)
        self.objs.append(pointy)
class diamond:
    def __init__(self, pos, scale = 1):
        w = 10 * scale
        p = Polygon(Point(pos.x-w/2, pos.y-w/4), Point(pos.x, pos.y-w), Point(pos.x+w/2, pos.y-w/4), Point(pos.x, pos.y+w/2 + 1 * scale))
        p.setFill("red")
        p.draw(win)
        self.objs = []
        self.objs.append(p)
class club:
    def __init__(self, pos, scale = 1):
        w = 10 * scale
        circ1 = Circle(Point(pos.x - w/3, pos.y - 2 * scale), 4 * scale)
        circ2 = Circle(Point(pos.x + w/3, pos.y - 2 * scale), 4 * scale)
        circ3 = Circle(Point(pos.x, pos.y - 6 * scale), 4 * scale)
        rect = Rectangle(Point(pos.x - 2 * scale, pos.y), Point(pos.x + 2 * scale, pos.y + 5 * scale))
        circ1.setFill("black")
        circ2.setFill("black")
        circ3.setFill("black")
        rect.setFill("black")
        self.objs = []
        self.objs.append(circ1)
        self.objs.append(circ2)
        self.objs.append(circ3)
        self.objs.append(rect)
        circ1.draw(win)
        circ2.draw(win)
        circ3.draw(win)
        rect.draw(win)
class spade:
    def __init__(self, pos, scale = 1):
        w = 10 * scale
        leftbump = Oval(Point(pos.x-9 * scale,pos.y+w/2), Point(pos.x+w/8, pos.y - w/2))
        rightbump = Oval(Point(pos.x + 9 * scale,pos.y+w/2), Point(pos.x-w/8, pos.y - w/2))
        rect = Rectangle(Point(pos.x - 2 * scale, pos.y), Point(pos.x + 2 * scale, pos.y + 7 * scale))
        pointy = Polygon(Point(pos.x - w + 1.2 * scale, pos.y - 2 * scale), Point(pos.x + w - 1.2 * scale, pos.y-2 * scale), Point(pos.x, pos.y-w))
        leftbump.setFill("black")
        rightbump.setFill("black")
        pointy.setFill("black")
        rect.setFill("black")
        self.objs = []
        self.objs.append(pointy)
        self.objs.append(leftbump)
        self.objs.append(rightbump)
        self.objs.append(rect)
        pointy.draw(win)
        leftbump.draw(win)
        rightbump.draw(win)
        rect.draw(win)
def drawPoints(pos,scale, x, i, points):
    i = i+1
    w = 10 * scale
    match i:
        case 1:
            p = x(Point(pos.x, pos.y-w/2), 0.2 * scale)
            points.append(p)
        case 2:
            undrawl(points[0].objs)
            points.pop(0)
            p = x(Point(pos.x, pos.y - w + 2 * scale), 0.1 * scale)
            p2 = x(Point(pos.x, pos.y - 1.5 * scale), 0.1 * scale)
            points.append(p)
            points.append(p2)
        case 3:
            p = x(Point(pos.x, pos.y - w/2), 0.1 * scale)
            points.append(p)
        case 4:
            for p in points:
                undrawl(p.objs)
            points = []
            p = x(Point(pos.x-1 * scale, pos.y - w + 2 * scale), 0.08 * scale)
            p1 = x(Point(pos.x+1 * scale, pos.y - w + 2 * scale), 0.08 * scale)
            p2 = x(Point(pos.x-1 * scale, pos.y - 1.5 * scale), 0.08 * scale)
            p3 = x(Point(pos.x+1 * scale, pos.y - 1.5 * scale), 0.08 * scale)
            points.append(p)
            points.append(p1)
            points.append(p2)
            points.append(p3)
        case 5:
            p = x(Point(pos.x, pos.y - w/2), 0.08 * scale)
            points.append(p)
        case 6:
            undrawl(points[-1].objs)
            points.pop(-1)
            p = x(Point(pos.x-1 * scale, pos.y - w/2), 0.08 * scale)
            p1 = x(Point(pos.x+1 * scale, pos.y - w/2), 0.08 * scale)
            points.append(p)
            points.append(p1)
        case 7:
            p = x(Point(pos.x, pos.y - w/2 - 1.5 * scale), 0.08 * scale)
            points.append(p)
        case 8:
            p = x(Point(pos.x, pos.y - w/2 + 1.75 * scale), 0.08 * scale)
            points.append(p)
        case 9:
            for i in range(4,8):
                undrawl(points[i].objs)
            p = x(Point(pos.x-1 * scale, pos.y-w/2 + 1 * scale), 0.08 * scale)
            p1 = x(Point(pos.x+1 * scale, pos.y-w/2 + 1 * scale), 0.08 * scale)
            p2 = x(Point(pos.x-1 * scale, pos.y-w/2 - 1 * scale), 0.08 * scale)
            p3 = x(Point(pos.x+1 * scale, pos.y-w/2 - 1 * scale), 0.08 * scale)
            p4 = x(Point(pos.x, pos.y - w/2), 0.08 * scale)
            points.append(p)
            points.append(p1)
            points.append(p2)
            points.append(p3)
            points.append(p4)
        case 10:
            undrawl(points[-1].objs)
            points.pop(-1)
            p = x(Point(pos.x, pos.y - w + 3 * scale), 0.08 * scale)
            p1 = x(Point(pos.x, pos.y - 2.75 * scale), 0.08 * scale)
            points.append(p)
            points.append(p1)
        case _:
            for p in points:
                undrawl(p.objs)
            points = []
    return points
class card:
    def __init__(self, card, pos, scale = 1):
        suit = card.getSuit()
        num = card.num
        name = card.getName()
        self.rawCard = card
        w = 10 * scale
        bg = Rectangle(Point(pos.x-w/3, pos.y-w), Point(pos.x+ w/3, pos.y))
        bg.setFill("white")
        bg.draw(win)
        color = "red"
        self.points = []
        self.pos = pos
        match suit:
            case "diamonds":
                x = diamond
                color = "red"
            case "spades":
                x = spade
                color = "black"
            case "hearts":
                x = heart
                color = "red"
            case "clubs":
                x = club
                color = "black"
        p1 = x(Point(pos.x-2.5 * scale, pos.y - w + 2.5 * scale), 0.08 * scale)
        p2 = x(Point(pos.x+2.5 * scale, pos.y - 2.2 * scale), 0.08 * scale)
        t1 = Text(Point(pos.x-2.5 * scale,pos.y - w + 1 * scale), str(num))
        t2 = Text(Point(pos.x+2.5 * scale,pos.y - 1 * scale), str(num))
        try:
            t1.setSize(int(ceil(8 * scale)))
            t2.setSize(int(ceil(8 * scale)))
            t1.setFill(color)
            t2.setFill(color)
            t1.draw(win)
            t2.draw(win)
        except:
            None
        for i in range(num):
               self.points = drawPoints(pos, scale, x, i, self.points)
        if num == 11:
            face = Circle(Point(pos.x, pos.y - w/2), 2 * scale)
            e1 = Circle(Point(pos.x-1*scale, pos.y - w/2), 0.25 * scale)
            e2 = Circle(Point(pos.x+1*scale, pos.y - w/2), 0.25 * scale)
            e1.setFill(color)
            e2.setFill(color)
            face.draw(win)
            e1.draw(win)
            e2.draw(win)
            self.points.append(e1)
            self.points.append(e2)
        elif num == 12:
            tri = Polygon(Point(pos.x, pos.y - w/2 - 2 * scale), Point(pos.x - 1 * scale, pos.y - w/2 + 2 * scale), Point(pos.x + 1 * scale, pos.y - w/2 + 2 * scale))
            tri.setFill(color)
            tri.draw(win)
            self.points.append(tri)
        elif num == 13:
            tri = Polygon(Point(pos.x, pos.y - w/2 - 1 * scale), Point(pos.x - 1 * scale, pos.y - w/2 + 1 * scale), Point(pos.x + 1 * scale, pos.y - w/2 + 1 * scale))
            tri.setFill(color)
            tri.draw(win)
            self.points.append(tri)
        if num == 1 or num>10:
            t1.setText(name[:1])
            t2.setText(name[:1])
        self.points.append(p1)
        self.points.append(p2)
        self.points.append(t1)
        self.points.append(t2)
        self.points.insert(0, bg)
        update()
