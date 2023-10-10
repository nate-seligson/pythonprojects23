from minesweeper import *
from time import sleep
from random import randrange
import pandas
covered = []
num = []
action = []
flagged = []
hasmine = []
squares = Run()
def CheckFlags(s):
    global flagged
    num = 0
    for x in s.l:
        if x.flagged:
            num+=1
    flagged += [num]
    if num == s.num:
        return True
    else:
        return False
def CalculateRevealed(s):
    ToFlag = []
    for x in s.l:
        if not x.revealed:
            ToFlag.append(x)
    return ToFlag
while True:
    x = squares[randrange(0,len(squares)-1)]
    if not x.hasMine and x.num == 0:
        x.reveal()
        break
update()
while True:
    i = 0
    nots = 0
    for s in squares:
        if s.revealed and s.num != 0:
            num += [s.num]
            x = CalculateRevealed(s)
            covered += [len(x)]
            if CheckFlags(s):
                for x in s.l:
                    if not x.revealed and not x.flagged:
                        x.reveal()
                        update()
                action += [2]
            elif len(x) == s.num and s.num != 0:
                for a in x:
                    if not a.flagged:
                        a.flag()
                update()
                action += [1]
            else:
                 action += [0]
        else:
            nots +=1
    dd = pandas.DataFrame(
    {"Covered": covered, "Flagged": flagged, "Num": num, "Action": action}
    )
    dd.to_csv("out.csv", index = False)
    print(nots)
    if nots == bombs:
        break
        
            
