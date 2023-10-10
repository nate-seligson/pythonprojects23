import random
def interpret(n):
    match n:
        case 1:
            return "ace"
        case 11:
            return "jack"
        case 12:
            return "queen"
        case 13:
            return "king"
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
