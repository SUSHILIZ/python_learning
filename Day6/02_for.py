#for loop
#used for sequential traversing. used for list, tupple, string etc

# for loops

# for el in list:
#      #some work

list=[1,2,3,4]
for el in list:
     print(el)


# for loops with else
# for el in list:
#      #some work
# else:
     #work whe loop ends

list=[1,2,3,4]
for el in list:
     if(el==3):
        print("3 found")
        break
     print(el)
else:
    print("end")

#else can be used when loop is completely used
#if we use break else donot execute

#see down program without using else
list=[1,2,3,4]
for el in list:
     if(el==3):
        print("3 found")
        break
     print(el)
print("end")

#WAP for for loop

list=[1,4,9,16,25,36,49,64,81,100]
for el in list:
     print(el)

#search for a number x in this turple using loop
# tuple=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("x:"))
# i=0
# for el in tuple:
#      if(el==x):
#           print(x,"is present at index",i)
#           break
#      else:
#           print("finding..")
#      i+=1

#range()

for el in range(5):
     print(el)

for el in range(1,5):
     print(el)

for el in range(1,5,2):
     print(el)


# using for and range()
#WAP to print numbers from 1 to 100
# for el in range(1,101):
     # print(el)

#WAP to print numbers from 100 to 1
for el in range(100,0,-1):
     print(el)

#print the multiplication table of a number n

# n=int(input("n:"))
# for el in range(1,11):
#      print(el*n)

#-------pass-----=>null statement that does nothing.It is used as placeholder for future code.

for ele in range(1,5):
     pass
print("some useful work")


#WAP to find the sum of first n numbers.
n=int(input("n:"))
i=1
sum=0
while i<=n:
     sum=sum+i
     i+=1
print("sum:",sum)

#WAP to find the factorial of first n numbers.

n=int(input("n:"))
prod=1
for el in range(1,n+1):
     prod=prod*el
print("fact:",prod)


#In this program, I learned about while,infinite loop, break, continue, for, for with else, range().
