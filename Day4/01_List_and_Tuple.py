#List         #same as array
# A built-in-data type that stores set of values(can store element of different types(int,float,str,etc))

items=["spiderman",84,99.99,"batman"]
print(items[0])
print(items[2])

items[0]="superman"  #allowed in python

print(items)

print(len(items))

#List Slicing
# similar to string slicing
marks=[1,2,3,4,5]

print(marks[0:3])
print(marks[2:])
print(marks[:2])

#List Methods
#append, sort, reverse,insert,remove,pop,count

list=[2,4,3]
list.append(5)
print(list) #=> 2,4,3,5

list1=[1,3,4,2]
list1.sort() #sorts in ascending order
print(list1) #=> 1,2,3,4

list2=[1,3,5,4]
list2.sort(reverse=True) #sorts in descending order
print(list2) #=>5,4,3,1

list3=[3,1,2]
list3.reverse() #reverse list
print(list3) #=> 2,1,3

list4=[1,2,4]
list4.insert(2,3) #insert 2 index 3
print(list4) #=> 1,2,3,4

list5=[5,6,1,7,8,1]
list5.remove(1) #removes first occurance of element
print(list5) #=>5,6,7,8,1

list6=[1,2,3,4]
list6.pop(2) #removes element at index
print(list6) #=>1,2,4

list7=[1,2,3,1,4,5,1]
print(list7.count(1))

# #WAP to ask the user to enter names of their 3 favourite movies and stores them in a list

# list=[]
# movie1=input("movie1:")
# movie2=input("movie2:")
# movie3=input("movie3:")
# list.append(movie1)
# list.append(movie2)
# list.append(movie3)
# print(list)


#WAP to check if a list contains a palindrome of elements
# list=[1,2,3,2,1]
# List=list.copy()
# List.reverse()
# if(list==List):
#     print("palindrome")
# else:
#     print("No palindrome")


#Tuples
# A built-in data type that lets us create immutable(cannot change) sequences of values.

tup=(87,64,33,95,76)

print(tup[0])

# tup[0]=45 #not allowed in py.
# print(tup)

tup1=()
tup2=(1,) #you cannot write (1) as it will understand as int not tuple.
# print(type(tup2))
tup3=(1,2,3)
# print(type(tup3))
# --------------Slicing is also possible in tuple------------
print(tup3[0:2])


#tuple methods
#index,count

tup=(2,1,3,1)
print(len(tup))

print(tup.index(1)) #returns index of first occurance
print(tup.count(1)) #counts total occurance

#WAP to count the numbers of students with "A" grade in the following tuple
["C","D","A","A","B","B","A"]

grade=("C","D","A","A","B","B","A")
print("No. of students with 'A' grade is:",grade.count("A"))

#Stores the above values in a list and sort them from "A" to "D"

list=["C","D","A","A","B","B","A"]
list.sort()
print(list)




#Note string and tuple are immutable(unchangeable) but list is mutuable(changeable)