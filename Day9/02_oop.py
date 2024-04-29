# OOP= Object Oriented programming

# let's discuss about class and object in python

#class is a blueprint for creating objects.

#creating class
#constructor or __init__ function
# we have default and parameterized constructor.
#creating Object(instance)
#methods are functions that belong to objects.
#data(or variable) stored inside class or object is attribute.

class Student:
    college_name="ABC college"          #this is class attribute

    def __init__(self,name,marks):   #in constructor we need to pass self argument.
        self.name=name               #self.something are object attribute
        self.marks=marks
    def printMe(self):                 #this is a method
        print("hello",self.name,"your marks is",self.marks)
        

s1=Student("sushil",32)        #here self and s1 produce same result
print(s1.name)
s1.printMe()
print(Student.college_name)

#create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def print_average(self):
        sum=0
        for el in self.mark:
            sum=sum+el
        print(self.name,"your average is",sum/3)


s1=Student("sushil",[90,98,96])
s1.print_average()



#----------Static Methods-----------------
# Methods that don't use the self parameter(work at class level)

class Student:
    @staticmethod #decorator
    def hello():
        print("hello")
s1=Student()
s1.hello()


# Important
# ----------------Abstraction-------------
#-----------------Encapsulation----------
#-----------------Inheritance------------
#-----------------Polymorphism-----------


#-----------Abstraction-----------
#Hiding the necessary implementation detail of a class and only showing essential features to the user.

class Car:
    def __init__(self):
        self.cla=False
        self.acc=False
        self.brk=False
    def start(self):
        self.cla=True
        self.acc=True
        print("car started")
car1=Car()
car1.start()

#-------------Encapsulation-----------
# Wrapping data and functions into a single unit(object)

#Create Account class with 2 attributes- balance and account no.
#create methods for debit, credit and printing the balance.

class Account:
    def __init__(self,balance,accountNo):
        self.balance=balance
        self.accountNo=accountNo
    def debit(self,amount):
        self.balance-=amount
        print(self.accountNo,"debited by Rs",amount)
        print("total balance=",self.bal())
    def credit(self,amount):
        self.balance+=amount
        print(self.accountNo,"credited by Rs",amount)
        print("total balance=",self.bal())

    def bal(self):
        return self.balance

acc1=Account(10000,1234567890)
acc1.debit(100)
acc1.credit(1000)