# Rock paper scissor
import random
userInp=input("R for Rock, P for Paper, S for Scissor:")
ran=random.choice(["R","P","S"])
if(userInp==ran):
    print("Tie,do again!")
elif(userInp=="R" and ran=="P"):
    print("computer choose",ran,".You lose❌")
elif(userInp=="P" and ran=="R"):
    print("Computer choose",ran,".You Win✅")
elif(userInp=="P" and ran=="S"):
    print("Computer choose",ran,".You lose❌")
elif(userInp=="S" and ran=="P"):
    print("Computer Choose",ran,".you win✅")
elif(userInp=="R" and ran=="S"):
    print("Computer Choose",ran,".you win✅")
elif(userInp=="S" and ran=="R"):
    print("Computer choose",ran,".You lose❌")
else:
    print("Error!.You can only click R or P or S")


