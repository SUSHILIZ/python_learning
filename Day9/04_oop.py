#             (many)
#-------------Polymorphism:Operator Overloading------------
#when the same thing can be used in different ways.


print(1+2) #3
print("sushil"+"subedi") #sushilsubedi #concatenate
print([1,2,3]+[4,5,6])   #[1,2,3,4,5,6] #merge

# This is an operator overloading as + varies according to data type.

#Operators and Dunder functions

#             (many)
#-------------Polymorphism:Operator Overloading------------
#when the same thing can be used in different ways.


print(1+2) #3
print("sushil"+"subedi") #sushilsubedi #concatenate
print([1,2,3]+[4,5,6])   #[1,2,3,4,5,6] #merge

# This is an operator overloading as + varies according to data type.

#Operators and Dunder functions
#a+b          a.__add__(b)
#a-b           a.__sub__(b)
#a*b           a.__mul__(b)
#a/b       a.__truediv__(b)
#a%b           a.__mod__(b)


#Let's understand through a example
# Add two complex numbers
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        print(self.real,"i+",self.img,"j")
    def __add__(self,num2):
        finalReal=self.real+num2.real
        finalImg=self.img+num2.img
        return Complex(finalReal,finalImg)
c1=Complex(1,2)
c1.show()

c2=Complex(3,4)
c2.show()

c3=c1+c2            #c3=c1.add(c2)  because of __
c3.show()

#Subtract two complex numbers
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        print(self.real,"i+",self.img,"j")
    def __sub__(self,num2):
        finalReal=self.real-num2.real
        finalImg=self.img-num2.img
        return Complex(finalReal,finalImg)
c1=Complex(5,6)
c1.show()

c2=Complex(3,4)
c2.show()

c3=c1-c2
c3.show()
