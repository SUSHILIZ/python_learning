# Basic Operations
# Concatenation
print("hello"+" "+"world")

# Length pf string 
str1="hello"
Length=len(str1)
print(Length)

#Indexing
str1="hello"
print(str1[0])
# str1[0]='i'   ##'str' object does not support item assignment


#Slicing(Acessing parts of a string)
str="helloWorld"
print(str[0:5]) #=>hello #starting index is included but not ending one.
print(str[:5]) #=>hello
print(str[0:]) #=>helloworld

# Negative index

str="Apple"
print(str[-3:-1]) #=>pl
print(str[-3:]) #=>ple
print(str[:-3]) #=>Ap

#String functions
str="Iam happy"
print(str.endswith("py")) #=>True
print(str.capitalize()) #=>capitalize first character
print(str.replace("happy","sad"))
print(str.find("happy")) #=>4 #returns first index of 1st occurrer
print(str.count("am")) #=>1 #counts the occurance of substring

# #program to input user first name and print its length
# name=input("name:")
# length=len(name)
# print("The length is",length)

#WAP to find occurance of '$' in a string
str="Hi,$Iam the $ symbol $99.99"
print(str.count("$"))

# #WAP to check if a number entered by user is odd or even
# num=int(input("Enter number:"))
# if(num%2==0):
#     print("Even")
# else:
#     print("Odd")

# #WAP to find greatest of 3 numbers entered by the user
# num1=int(input("Enter 1st number:"))
# num2=int(input("Enter 2nd number:"))
# num3=int(input("Enter 3rd number:"))
# if(num1>num2 and num1>num3):
#     print(num1,"is greatest")
# elif(num2>num1 and num2>num3):
#     print(num2,"is greatest")
# else:
#     print(num3,"is greatest")

#WAP to check if a number is multiple of 7 or not

num=int(input("Enter number to check:"))

if(num%7==0):
    print(num, "is multiple of 7")
else:
    print(num, "is not multiple of 7")