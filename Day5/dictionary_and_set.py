#Dictionary
#They are used to store data values in key:value pairs
#They are unordered, mutuable(changeable), duplicate keys not allowed.

info={
    "name":"Sushil",
    "cgpa":3.8,
    "marks":[80,86,90]
}
print(info["name"])

info["name"]="Sarala"  #mutuable
info["username"]="saralasubedi"  #We can add another key-value pair

print(info)


null_dict={}
null_dict["name"]="hero"
print(null_dict)

#Nested Dictionaries
student={
    "name":"sushil",
    "score":{
        "chem":97,
        "math":96,
        "physics":98
    }
}
 
print(student["score"])
print(student["score"]["chem"])

#Dictionary Methods
# keys,values,items,get,update

info={
    "name":"Sushil",
    "cgpa":3.8,
    "marks":[80,86,90]
}

print(len(info.keys()))
print(info.keys()) 

# we can convery dict into list and tup.=>typecasting
print(list(info.keys()))

print(info.values())
print(tuple(info.values()))


print(info.items())  #returns all (key,val) pairs as tuples.


print(info.get("name")) #no error=>best practice.
print(info["name"]) #error

info.update({"name":"sarala","username":"sushilsubedi"}) #insert specific items to the dictionary.
print(info)

#-----------set---------=>set is mutuable(unhashable) but element is immutable(hashable)
# set is collection of unorder items
#Each element in the set must be unique and immutable.(list and dictionary cannot be used.)

collection={1,2,3,"hello","hello","world",4}
#dublicate value ignored #not in order
print(collection)
print(type(collection))
print(len(collection))

collection={} #this is empty dict
print(type(collection))

# So inorder to create set
collection=set()
print(type(collection))

# Set Methods
#add,remove,clear,pop

collection={1,2,3,4,5}
collection.add(6) #add element
print(collection)

collection2={1,2,3,4,5}
collection2.remove(3) #remove element
print(collection2)

collection3={1,2,3,4,5}
collection3.clear() #empties the set
print(collection3)

collection4={"hari","shyam","gita","laxman","sushil"} #removes a random value
print(collection4.pop())
print(collection4)
print(collection4.pop())
print(collection4)


#important method in set
set={1,2,3,4}
set1={4,5,6,7}
print(set.union(set1))
print(set.intersection(set1))


#practice question
# 1.
# dict={}
# dict["table"]="a piece of furniture","list of facts and figures"
# dict["cat"]="a small animal"
# print(dict)

# or

dict={
    "table":("a piece of furniture","list of facts"),
    "cat":"a small animal"
}
print(dict)



# 2.
list={"python","java","c++","python","javascipt","java","python","java","c++","c"}

#as set ignored duplicate values

print("No.of classroom needed",len(list))

# 3.
# mark1=int(input("Enter marks of subj1:"))
# mark2=int(input("Enter marks of subj2:"))
# mark3=int(input("Enter marks of subj3:"))

# # dict={}
# # dict.update({"sub1":mark1,"sub2":mark2,"sub3":mark3})
# # print(dict)

# dict={}
# dict.update({"sub1:":mark1})  
# # dict["subj1:"]=mark1 we can do by this way also.
# dict.update({"sub2:":mark2})
# dict.update({"sub3:":mark3})
# print(dict)

#Figure out a way to store 9 and 9.0 as seperate values in the set.
#(you can take help of built in data types)
set={9,"9.0"}
print(set)

set={("int",9),("float",9.0)}
print(set)

#---------------------------immutuable= tuple, string, elements of set-------------------------------------
#----------------------------mutuable= list, dictionary, set------------------------------------------------



















