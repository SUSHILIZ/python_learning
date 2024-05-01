# del keyword
# used to delete object properties (attributes) or object itself

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("sushil",23)
print(s1.name)
del s1.name
print(s1.age)
# print(s1.name)


# Private(like) attributes and methods
#for making private use __
#give acesss within class and cannot get access outside class
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    def reset(self):
        print(self.__acc_pass)

acc1=Account("12345","abcde")
print(acc1.acc_no)
acc1.reset()
# print(acc1.__acc_pass)

#we can make method also private
class Person:
    __name="sushil"

    def __hello(self):
        print("hello")

    def welcome(self):
        self.__hello()      #private method can access inside class.

p1=Person()
# # p1.__name
# # p1.__hello()
p1.welcome()

#Inheritance
#when one class(Child/derived) derives the properties and methods of another class(parent/base).
 
# syntax

# class Car():
#     ............

# class ToyotaCar(Car):
#     ..............


class Car:   #parent (base)
    color="black"    #property (attribute)
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():           #method
        print("Car stopped")

class toyotaCar(Car):      #child (derived)
    def __init__(self,name):
        self.name=name
    def message(self):
        print("New Car")

car1=toyotaCar("fortuner")
car1.start()
print(car1.color)

# toyotaCar can access the properties and methods of car


#Types of Inheritance
#1.Single Inheritance  
    #have one base(parent) and one derived(child)
    #Above is the example of this type of Inheritance

#2.Multi-level Inheritance

    #Base 1

    #Derived 2(this can access property and method of 1)

    #Derived 3 (this can access property and method of 1 and 2)

#example

class Car:  
    color="black"   
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():          
        print("Car stopped")

class ToyotaCar(Car):     
    def __init__(self,brand):
        self.brand=brand
    def message(self):
        print("New Car")

class Fortuner(toyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fortuner("diesal")
car1.start()
car1.message()

#Fortuner can access method and property of Car and ToyotaCar.


#3.Multiple Inheritance
  
#  (par1)   (par2)
# Base 1     Base 2

        #Derived 
        #  (child)

class A:
    varA="welcome to class  A"

class B:
    varB="Welcome to class B"

class C(A,B):
    varC="Welcome to class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)


#Super method
#used to access methods of the parent class.

class Bike:
    def __init__(self,type):
        self.type=type
    def Stop(self):
      print("Bike stopped...")

class Honda(Bike):

    def __init__(self,name,type):
       self.name=name
       super().__init__(type)

    def stop(self):
       super().Stop()

honda=Honda("Aventon","electric")
print(honda.type)
honda.stop()


#-----------class method-----------

 # A class method is bound to the class and receives the class as an implicit first argument.
 # Note:::: static method can't access or modify class state and generally for utility.

 #static method(@staticmethod is only used if there is no class attribute and instance(object) attribute)


class Person:
    name="sushil"
    @classmethod  #decorator  #it can  change class attrubute
    def changeName(cls,name):
        cls.name=name
p1=Person()
p1.changeName("hero")
print(Person.name)
print(p1.name)


#There are three types of methods inside the classes
# static methods
# class methods(cls)
# instance methods(self)


#property decorator
#    It helps to convert method into attribute

class Student:
    def __init__(self,math,phy,chem):
        self.math=math
        self.phy=phy
        self.chem=chem
    @property
    def percentage(self):
        return str((self.math+self.phy+self.chem)/3)+"%"

s1=Student(98,97,99)
print(s1.percentage)
s1.phy=83
print(s1.phy)
print(s1.percentage)


#explanation
# This also give same result but above is recommended
class Student:
    def __init__(self,math,phy,chem):
        self.math=math
        self.phy=phy
        self.chem=chem
    def channgepercentage(self):
        return str((self.math+self.phy+self.chem)/3)+"%"
s1=Student(98,97,99)
print(s1.channgepercentage())
s1.phy=83
print(s1.phy)
print(s1.channgepercentage())


#----We have studied @staticmethod, @classmethod, @property decorators-------

