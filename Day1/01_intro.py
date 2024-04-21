print("Hello world\nIam Sushil")


# variables(name given to memory location in the program)

name="sushil"
age=23
price=99.99

print(price)
print("My name is:",name)
print("My age is:",age)

# Note in py backtick cannot be used (``)

# Identifier(name of variable, functions etc)
'''An identifier in Python starts with a letter (A-Z or a-z) or an underscore (_) followed by any number of letters, digits (0-9), or underscores.'''

print(type(name))
print(type(age))
print(type(price))


# Datatypes
'''
1.Integer +ve -ve 0  =>int
3.Float =>9.99 5.67
2.string
4.Boolean => True False (Start with capital)
5.None
'''
age=23
old=False
a=None
print(type(old))
print(type(a))

# keywords(Reserved words in py)
# e.g: and as def if else except finally in is True return None etc

# python is a case sensitive=> uppercase and lowercase matter

# ----------print sum--------------

a=2
b=3
sum=a+b
print(sum)

# TYpes of Tokens
#Punctuators(symbols to organize sentence structure)
# {},[],(),@,# etc and also includes  agumented assignment operators(-=,+=,/=,*=,//=,=)

# python is a implicit typed language
# age=23

#java, c++ is a explicit typed language
# int age=23

#Expression Execution
#string and Numeric values can operate with * =>Repeat
print("@"*6) #@@@@@@
#string and string can operate with + =>Concatenation
print(("2"+"@")*3) #2@2@2
#Numeric values can operate with all arithmetic operators
print(2+3*4) #14
#Arithmetic expression with Integer and float will result in float
print(2*3.0) #=>6.0
print(2+3.0) #=>5.0
#Result of division operator(/) with two integers will be float
print(2/3) #=>0.6666666666666666
print(3/2) #=>1.5
#Integer division with float and int will give int dispayed as float
print(2//3.0) #=>0.0
print(3.0//2) #=>1.0
#Integer division with two integers will give int
print(2//3) #=>0
print(3//2) #=>1
 # result of (A//B is same as floor(A/B))

#Remainder is negative when denominator is negative
print(-5%2) #=>1
print(5%-2) #=>-1

# --------Comments in py-------
# This is a comment
# for more than one comment

'''Print("first Statement)
print("Second statement)'''
