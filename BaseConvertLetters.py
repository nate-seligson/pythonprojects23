from threading import *
dic = open("popular.txt", "r").read().splitlines()
fin = open("converions.txt", "w")
class Num:
    def __init__(self, raw, b):
        self.n = BaseConvert(raw,b).lower()
        self.b = b
def Convert(x):
    c = chr(97 + (x-10)).upper()
    return c

def BaseConvert(n, b):
    n = int(n)
    b = int(b)
    answer = ""
    if n != 0 and n != b:
        x = n % b
        if x > 9 and x < b:
            y = Convert(x)
        elif 10 >= x >= b:
            return False
        else:
            y = x
            return False
        try:
            answer = BaseConvert((n-x) // b, b) + str(y)
        except:
            return False
    return answer
def Reverse(inp, b):
    final = 0
    i = 0
    try:
        int(inp)
        return
    except:
        for s in inp[::-1]:
            amt = ord(s)-87
            if amt >= b:
                return False
            amt *= b**i
            final+=amt
            i+=1
    i = 11
    possibles = []
    while i < 36:
        if BaseConvert(final,i) != False and i != b:
            try:
                possibles.append(Num(final,i))
            except:
                continue
        i+=1
    for d in dic:
        for p in possibles:
            if d == p.n:
                fin.write(inp.upper() +" "+ str(b) + " converts to "+p.n.upper()+" "+ str(p.b)+"\n")
iterator = 0
def Load():
    while True:
        global iterator
        print(str((iterator/len(dic))*100) + "% complete")
def Start():
    global iterator
    for d in dic:
       iterator+=1
       for i in range(11,36):
            Reverse(d,i)
    fin.close()
l = Thread(target = Load, daemon = True)
s = Thread(target = Start, daemon = True)
l.start()
s.start()
print("done")
