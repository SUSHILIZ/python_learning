#while
# while condition:
#     #some work

#WAP to print hello 5 times
i=1           #Here i is iterator and this process is iteration
while i<6:
    print("hello")
    i+=1


#WAP to print from 1 to 5
i=1
while i<6:
    print(i)
    i+=1

#WAP to print from 5 to 1
i=5
while i>=1:
    print(i)
    i-=1


#infinite loop  #so dangerous

# i=5
# while i<6:
    # print(i)
    # i-=1

#WAP to print numbers from 1 to 100

i=1
while i<=100:
    print(i)
    i+=1

#print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1

#print multiplication table of number n.

# n=int(input("multiplication table of:"))
# i=1
# while i<=10:
#     print(i*n)
#     i+=1

#print the elements of the following list using a loop
list=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(list):
    print(list[i])
    i+=1

#search for a number x in this turple using loop
# tuple=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("x:"))
# i=0
# while i<10:
#     if(tuple[i]==x):
#         print(x,"is present")
#         break
#     else:
#         print("finding..")
#     i+=1



#break stops the iteration
i=1
while i<=5:
        if(i==4):
             break
        print(i)
        i+=1

#continue
i=1
while i<=5:
        if(i==4):
             i+=1
             continue #skip
        print(i)
        i+=1


# Due to headache, today I stop here. Tommorrow I will learn for loop