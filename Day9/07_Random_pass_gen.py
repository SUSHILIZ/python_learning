#Random Password Generator
import random
import string

charVal=string.ascii_letters + string.digits +string.punctuation
n=int(input("n:"))
# password=""
# for el in range(n):
#     rand=random.choice(charVal)
#     password+=rand

#using list comprehension
password="".join([random.choice(charVal) for el in range(n)])

print("Your generated random password is",password)