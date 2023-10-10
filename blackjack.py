import random
import math
removalList = []
def DrawCard():
    global removalList
    cardList = []
    for i in range(0,53):
        if removalList.count(i) == 0:
            cardList.append(i)
    x = random.randint(0,len(cardList)-1)
    try:
      removalList.append(cardList[x])
    except:
        print(x)
    m = math.floor((cardList[x]/13))
    b = cardList[x] - (13 * m) - 9
    match m:
        case 0:
            end = "Of Hearts"
        case 1:
            end = "Of Diamonds"
        case 2:
            end = "Of Clubs"
        case 3 | 4:
            end = "Of Spades"
    match b:
        case 0:
            final = "Jack"
        case 1:
            final = "Queen"
        case 2:
            final = "King"
        case 3:
            final = "Ace"
        case _:
            final = str((cardList[x] - (13 * m)) + 2)
    final += " " + end
    return final
def Convert(n):
    x = n[:4]
    final = ""
    for i in x:
        try:
            final += str(int(i))
        except:
            match i:
                case "J" | "Q" | "K":
                    final = "10"
                    return int(final)
                case "A":
                    final = "11"
                    return int(final)
    return int(final)
def BlackJack():
    num = 0
    x = DrawCard()
    print("Fist card: " + x)
    num += Convert(x)
    while True:
        inp = input("Hit or stay?")
        if inp == "hit" and num < 21:
            x = DrawCard()
            num += Convert(x)
            print("new card: " + x)
            if num > 21:
                print("Bust!")
                return
            elif num == 21:
                print("Blackjack! You win")
                return
        elif inp == "stay" and num < 21:
            houseNum = 0
            while houseNum < 21:
                y = DrawCard()
                print("House draws: " + y)
                houseNum += Convert(y)
                if houseNum > num and houseNum <= 21:
                    print("House wins, " + str(houseNum))
                    return
            print("House Busted. You win!")
def drawWar(scale):
    x = DrawCard()
    y = DrawCard()
    print("p1 draws:" + x)
    print("p2 Draws:" + y)
    if Convert(x)>Convert(y):
        print("p1 Wins!")
        return "p1", scale
    elif Convert(x)<Convert(y):
        print("p2 Wins!")
        return "p2", scale
    else:
        print("War!")
        for i in range(2):
            DrawCard()
        return drawWar(scale + 3)
def War():
    p1 = 0
    p2 = 0
    while True:
       try:
            w = drawWar(1)
            if w[0] == "p1":
                p1 += w[1]
            else:
                p2 += w[1]
            inp = input("Next?")
       except:
            print("game end!")
            if p1>p2:
                print("p1 wins whole game! " + str(p1) + " Points!")
            else:
                print("p2 wins game! " + str(p2) + " Points!")
            print(p1)
            print(p2)
            return
