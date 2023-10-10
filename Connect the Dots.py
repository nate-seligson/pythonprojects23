from graphics import *
win = GraphWin("THE GRAPH", 800,600)
x = Entry(Point(100,100), 15)
x.draw(win)
def interpret(x):
    numList = []
    for i in range(x):
        c = Circle(win.getMouse(), 10)
        c.draw(win)
        c.setFill("white")
        numList.append(c)
        t = Text(c.getCenter(), str(numList.index(c) + 1))
        t.draw(win)
    for i in range(int(len(numList))):
        l = Line(numList[i].getCenter(), numList[i-1].getCenter())
        l.setFill("red")
        l.draw(win)
while True:
      if win.getKey() == "Return":
          interpret(int(x.getText()))
      
