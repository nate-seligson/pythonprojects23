import random
from graphics import *
from cardVis import *
import math
win = GraphWin("THE GRAPH", 800,800, False)
init(win)
win.setBackground("green")
bottom = 100
right = 100
win.setCoords(0,bottom,right,0)
def interpret(n):
    match n:
        case 1:
            return "Ace"
        case 11:
            return "Jack"
        case 12:
            return "Queen"
        case 13:
            return "King"
        case _:
            return str(n)
class Card:
    def __init__(self, num, suit):
        if suit == "diamonds" or suit == "clubs" or suit == "hearts" or suit == "spades":
            if 1 <= num <= 13:
                nameNum = interpret(num)
                nameSuit = " of " + suit
            else:
                nameNum = "joker"
                nameSuit = ""
                suit = None
            self.name = nameNum + nameSuit
            self.num = num
            self.suit = suit
        else:
            print("not a valid suit")
    def getNum(self):
        if self.num == 1:
            return 11
        return self.num
    def getSuit(self):
        return self.suit
    def getName(self):
        return self.name
    def getColor(self):
        if self.suit != None:
            if self.suit == "clubs" or self.suit == "diamonds":
                return "red"
            else:
                return "black"
        else:
            return None
class Deck:
    def __init__(self):
        self.pile = []
        for x in range(2):
            for i in range(13):
                if x == 0:
                    self.pile.append(Card(i + 1,"hearts"))
                else:
                    self.pile.append(Card(i + 1, "clubs"))
        for x in range(2):
            i = 13
            while i >= 1:
                if x == 0:
                    self.pile.append(Card(i,"diamonds"))
                else:
                    self.pile.append(Card(i, "spades"))
                i = i-1
    def draw(self, num = 1):
        cs = []
        for i in range(num):
            cs.append(self.pile[0])
            self.pile.remove(self.pile[0])
        return cs
    def shuffle(self):
        for i in range(len(self.pile)):
            r = random.randint(0,len(self.pile) - 1)
            c1 = self.pile[i]
            c2 = self.pile[r]
            self.pile[i] = c2
            self.pile[r] = c1
    def replace(self, cards):
        for i in cards:
            self.pile.append(i)
    def getSize(self):
        return len(self.pile)
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.finalData = []
    def getName(self):
        return self.name
    def draw(self, deck, num):
        x = deck.draw(num)
        for i in x:
            self.hand.append(i)
    def play(self, index = 0):
        return self.hand[0]
    def collect(self, cards):
        for i in cards:
            self.hand.append(i)
    def dispHand(self):
        c = []
        for i in self.hand:
            c.append(i.name)
        return c
def setTheStage(name):
    n = Text(Point(50,80), name)
    n.setSize(30)
    n.draw(win)
    hitButton = Rectangle(Point(25,85), Point(45, 90))
    stayButton = Rectangle(Point(55, 85), Point(75, 90))
    table = Rectangle(Point(0,30), Point(100, 75))
    table.setFill("saddlebrown")
    hitButton.setFill("khaki")
    stayButton.setFill("khaki")
    hitText = Text(Point(35, 87.5), "Hit")
    stayText = Text(Point(65, 87.5), "Stay")
    hitText.setSize(15)
    stayText.setSize(15)
    table.draw(win)
    hitButton.draw(win)
    stayButton.draw(win)
    hitText.draw(win)
    stayText.draw(win)
    update()
def BlackJack():
    t = Text(Point(50,10), "")
    t.setSize(30)
    t.draw(win)
    update() 
    num = 0
    deck = Deck()
    deck.shuffle()
    player = Player(input("Player name?"))
    player.draw(deck, 1)
    setTheStage(player.name)
    c1 = card(player.hand[0], Point(20,75), 2)
    if player.hand[0].getNum() > 10:
        num += 11
    else:
        num += player.hand[0].getNum()
    i = 0
    while True:
        inp = None
        c = win.checkMouse()
        if c != None:
            if 25 <= c.x <=45 and 85 <= c.y <= 90:
                inp = "hit"
            elif 55 <= c.x <= 75 and 85 <= c.y <= 90:
                inp = "stay"
        if inp == "hit" and num<21:
            inp = None
            i += 20
            player.draw(deck, 1)
            if player.hand[-1].getNum() > 10:
                num += 11
            else:
                num += player.hand[-1].getNum()
            card(player.hand[-1], Point(20 + i,75), 2)
            print("new card: " + player.hand[-1].getName())
            if num > 21:
                for h in player.hand:
                    if h.num == 1:
                        num -= 10
                        h.num = 2
                        break
                if num > 21:
                    t.setText("Bust!")
                    return
            elif num == 21:
                t.setText("blackjack! you win!")
                return
        elif inp == "stay" and num < 21:
            inp = None
            i = 0
            house = Player("House")
            houseNum = 0
            while houseNum < 21:
                i+=20
                house.draw(deck, 1)
                print("House draws:" + house.hand[-1].getName())
                card(house.hand[-1], Point(i, 50), 2)
                houseNum += house.hand[-1].getNum()
                if houseNum > num and houseNum <= 21:
                    t.setText("House wins, " + str(houseNum))
                    return
            for h in house.hand:
                if h.num == 1:
                    houseNum -= 10
                    h.num = 2
                    break
                if houseNum > 21:
                    t.setText("House Busted. You win!")
                    return
BlackJack()
                
    
