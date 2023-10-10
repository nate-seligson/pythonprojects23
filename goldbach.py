from math import *
def checkPrime(num):
  for i in range(2, ceil(sqrt(num))):
       if num % i == 0:
         return False
  return True
def findPrimes(num):
    checkValidity = lambda x: True if x > 0 and x % 2 == 0 else False
    totalString = ""
    if(not checkValidity(num)):
      return "Input a valid number!"
    for i in range(1, int(num/2) + 1):
      if checkPrime(num-i) and checkPrime(i):
          totalString += str(i) + " + " + str(num-i) + ", "
    return "Possible combinations: " + totalString[:-2]
while(True):
  print(findPrimes(int(input("pick a positive, even integer"))))
