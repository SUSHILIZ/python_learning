#Guess the Number.

import random

randNum=random.randint(1,100)
print("You have 10 attempt to guess right number")
for el in range(0,10):
    userNum=int(input("Guess the number:"))
    if(userNum==randNum):
        print(userNum, "is a correct guess")
        break
    elif(userNum<randNum):
        print("Your number was too small.Guess again!")
    else:
        print("your number was too large.Guess again!")
  

print("------------Game end----------------")