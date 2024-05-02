#practice Set
class Circle:
    def __init__(self,r):
        self.r=r
    def Area(self):
        print("Area of circle is",(22/7)*(self.r)**2)
    def Perimeter(self):
        print("Perimeter of circle is",2*(22/7)*self.r)
c1=Circle(21)
c1.Area()
c1.Perimeter()
    
class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showDetails(self):
        print("role=",self.role)
        print("department=",self.department)
        print("salary=",self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("accountant","finance",23000)

en=Engineer("sushil",23)
en.showDetails()


class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,ord2):
        return self.price>ord2.price

        
    
ord1=Order("pizza",1000)
ord2=Order("momo",100)
print(ord1>ord2)