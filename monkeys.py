from random import randint, choice
import Loader
def MonkeyName():
    monkey_name = ""
    for i in range(4):
        if i % 2 != 0:
            monkey_name += choice(vowels)
        else:
            letter = 'a'
            while letter in vowels:
                letter = randletter();
            monkey_name += letter
        if i == 0:
            monkey_name = monkey_name.upper()
    return monkey_name
vowels = ['a','e','i','o','u']
randletter = lambda: chr(97 + randint(0,25))
name = MonkeyName();
print("your monkey is named " + name + "!");
hours = int(input("how many hours do you want " + name +  " to work?"))
def WriteShakespeare():
    text_length = randint(1,1000 * hours)
    text = ""
    for t in range(text_length):
        sentence_length = randint(3,10)
        sentence = ""
        for s in range(sentence_length):
            word_length = randint(1,15)
            word = ""
            for w in range(word_length):
                word += randletter().upper() if s == 0 and w == 0 else randletter();   
            word += " "
            sentence += word
        sentence = sentence[::-1].replace(sentence[-1],choice(['.',',','?','!']),1)[::-1]
        sentence += " "
        text += sentence
    return text
def PullDictionary(txt):
    f = open(txt, 'r').read().lower()
    return f
def Compare(d1, d2):
    d2 = d2.split()
    words_found = 0
    words = []
    Loader.setLoader(len(d1.split()), "Finding")
    for s in d1.lower().split():
        if s in d2 and s not in words:
            words.append(s)
            words_found +=1
        Loader.iterator +=1
    return {'words found': words_found, 'words': words, }
def AddToFile(words, dic):
    f = open('hamlet_attempt', 'r')
    newWords = []
    split = f.read().split()
    for w in words:
        if w not in split:
            newWords.append(w)
    print("New words: "+ str(newWords))
    for w in split:
        if w not in words:
            words.append(w)
    f.close()
    f = open('hamlet_attempt', 'w')
    dic = dic.replace("\n", " linebreak")
    for w in dic.split():
        if w in words or w == "linebreak":
            if w == "linebreak":
                w = "\n"
            f.write(w + " ")
        else:
            space = ""
            for i in range(len(w)):
                space += " "
            f.write(space)
    f.close()
Loader.startLoader()
Loader.stop = False
w = WriteShakespeare()
print(w)
dic = PullDictionary('hamlet.txt')
c = Compare(w,dic)
print(c["words found"])
AddToFile(c['words'], dic)
print("File progressed saved as 'hamlet_attempt.txt'. ")
Loader.stop = True
name = MonkeyName();
print("This monkey is named " + name + "!");
