#List comprehension

# It is used to iterate over the list.

#example
 
list=[i for i in range(10)]
print(list)



# syntax
# newList=[expression(element) for element in oldList if condition]

list=[1,2,3,5]
newList=[i**2 for i in list]
print(newList)