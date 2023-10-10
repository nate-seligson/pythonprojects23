import math
import random
def isPrime(num):
    for i in range(2, math.ceil(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True
def generate():
    while True:
        p = random.randint(0,999)
        q = random.randint(0,999)
        if isPrime(p) and isPrime(q):
            break
    return p,q
def findE(lcm):
    for i in range(3,lcm):
        if math.gcd(i,lcm) == 1:
            return i
def findD(lcm,e):
    for i in range(1,lcm):
        if (i * e) % lcm == 1:
            return i
p,q = generate()
n = p * q
lcm = math.lcm(p-1,q-1)
e = findE(lcm)
d = findD(lcm,e)
print("public:  ", "e:", e, "n:", n)
def encode(message,ee = e,nn = n):
    if type(message) == str:
        newlist = []
        for m in message:
            newlist.append(ord(m)-96)
        message = newlist
    else:
        message = [message]
    encrypted = [(m ** ee) % nn for m in message]
    return encrypted
def decode(message,dd = d,nn = n):
    decrypted = [(m ** dd) % nn for m in message]
    final = ''
    for d in decrypted:
        final += chr(d + 96)
    decrypted = final
    return decrypted
