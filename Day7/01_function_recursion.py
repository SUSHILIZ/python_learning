# Fuction=> block of statements that perform a specific task

# def fuc_name(param1,param2,..):   =>Function Definition
#     #Some work
#     return val

# fuc_name(arg1,arg2,..)             =>Function call



#WAP to add two numbers
def sum(a,b): #a and b are parameter
    s=a+b
    return s
print(sum(2,3)) #2 and 3 are argument

# There are two types of functions i.e Built-in Functions(print(),len(),type(),range()) and User defined functions

#average of 3 numbers
def average(a,b,c):
    av=(a+b+c)/3
    return av
print(average(1,2,3))




# Default parameters
# Assigning a default value to parameter, which is used when no  argument is passed

#prod of two numbers
def cal_prod(a=2,b=5):
    print(a*b)
cal_prod()
cal_prod(2,4)


#Practice time😂
#WAP to print length of a list.(list is the parameter)

cities=["pokhara","kathmandu","biruta","dhankuta","bhairawa"]


def cal_length(list):
    print(len(list))
cal_length(cities)

#WAP to print the elements of a list in a single line. (list is the parameter)

# cities=["pokhara","kathmandu","biruta","dhankuta","bhairawa"]

# def print_element(list):
#     for el in list:
#         print(el,end=" ")  #by default, it has /n so we don't write

# print_element(cities)


#WAP to find the factorial of n.(n is the parameter)
# def cal_factorial(n):
#     prod=1
#     for el in range(1,n+1):
#         prod=prod*el
#     print("factorial of",n,"is",prod)

# cal_factorial(7)


#WAP to convert USD into NPR

def Convert(x):
    print(x,"USD","=",x*133.12,"NPR")

Convert(1000)


#WAP to check odd or even using function
# n=int(input("Enter a number to check:"))
# def Check(x=n): #I just use default parameter
#     if(x%2==0):
#         print("Even")
#     else:
#         print("ODD")

# Check()

#Recursion
#when a function calls itself repeatedly.

#print n to 1 backward

def show(n):
    if(n==0):  #=>base cap
        return
    print(n)
    show(n-1)
show(5)

#factorial using recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)
    
print(fact(7))

#Write a recursive function to calculate the sum of first n natural numbers

def sum(n):
    if(n==0):
        return 0
    return n+sum(n-1)
print(sum(10))


#Write a recursive function to print all elements in a list
#Hint: use list and index as parameter

def print_list(list,index=0):
    if(index==len(list)):
        return
    print(list[index])
    print_list(list,index+1)

cities=["pokhara","kathmandu","bhairava","chitwan","lalitpur"]
print_list(cities)