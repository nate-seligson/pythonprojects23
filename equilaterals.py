from graphics import *
import random
import math
from time import sleep
win = GraphWin("THE GRAPH", 800,800, False)
bottom = 100
right = 100
win.setCoords(0,bottom,right,0)
radius = 1
distance = lambda p1,p2: math.sqrt( ((p2.x-p1.x)**2) + ((p2.y-p1.y)**2) )
midpoint = lambda p1,p2: Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)
slope = lambda p1,p2: (p1.y-p2.y)/(p1.x-p2.x)
class player:
    def __init__(self, startpos):
        self.obj = Circle(startpos, radius)
        self.color = "red"
        self.obj.setFill(self.color)
        self.obj.draw(win)
        self.partners = []
        self.lines = []
        self.pos = startpos
        self.movePos = Point(0,0)
    def redraw(self):
        self.obj.undraw()
        self.obj = Circle(self.pos, radius)
        self.obj.setFill(self.color)
        self.obj.draw(win)
    def findPartners(self,playerList):
        self.partners = [playerList[random.randint(0,len(playerList)-1)] for i in range(2)]
        while self in self.partners:
            self.partners = [playerList[random.randint(0,len(playerList)-1)] for i in range(2)]
    def getPartnerDistance(self):
        d = distance(self.partners[0].pos, self.partners[1].pos)
        check = distance(self.partners[0].pos, self.pos) + distance(self.partners[1].pos, self.pos)


        wiggleroom = 10


        
        if d*2 <= check + wiggleroom and d*2 >= check - wiggleroom:
            self.movePos = self.pos
            return
        m = midpoint(self.partners[0].pos, self.partners[1].pos)
        distance_between = math.sqrt( (d**2) - ((d/2)**2))
        try:
            slp = -1/slope(self.partners[0].pos, self.partners[1].pos)
        except:
            slp = 0
        dx = distance_between/math.sqrt(1 + (slp*slp))
        dy = dx * slp
        newp = Point(m.x - dx, m.y - dy)
        newp2 = Point(m.x + dx, m.y + dy)
        self.movePos = newp if distance(newp,self.pos)<distance(newp2,self.pos) else newp2
    def moveToPoint(self):
        if self.pos == self.movePos:
            self.color = "blue"
            if len(self.lines) == 0:
                for p in self.partners:
                    l=Line(self.pos, p.pos)
                    self.lines.append(l)
                    l.draw(win)
            self.redraw()
            return
        if len(self.lines) > 0:
            for l in self.lines:
                l.undraw()
            self.color = "red"
            self.lines = []

            
        speed = distance(self.movePos, self.pos)/50


        
        direction = slope(self.pos,self.movePos)
        dx = speed / math.sqrt(1 + (direction*direction))
        dy = dx * direction
        self.pos = Point(self.pos.x - dx, self.pos.y - dy) if self.pos.x > self.movePos.x else Point(self.pos.x + dx, self.pos.y + dy)
        self.redraw()
circs = [player(Point(random.uniform(0,right), random.uniform(0,bottom))) for i in range(500)]
for c in circs:
    c.findPartners(circs)
    c.getPartnerDistance()
update()
randint = random.randint(0,len(circs)-1)
while True:
    for c in circs:
        c.moveToPoint()
    update()
    for c in circs:
        c.getPartnerDistance()
