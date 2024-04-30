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
