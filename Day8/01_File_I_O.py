#--------File I/O in python---------

# python can be used to perform operations on the file(read and write data)

#  Types of all Files
#1.Text files: .txt,.docx,.log etc.
#2. Binary files: .mp4, .mov, .png, .jpeg etc.

# Open, read and close File
#we have to open a file before reading or writing.

# f=open("file_name","mode")

# e.g file_name can be sample.txt , demo.docx etc
# mode can be r (read mode) ,w (write mode)
#mode is set to read mode by default

# data=f.read()
# f.close()


#example
# f=open("Day8/08_demo.txt","r")
# # f=open("Day8/08_demo.txt","rt") #same as 23
# data=f.read()
# # data=f.read(5) #read 5 character including space too.
# print(data)
# print(type(data))
# f.close()


#----------Reading a file-----------

# data=f.read() #reads entire file
# data=f.readline() #reads one line at a time
# f=open("Day8/08_demo.txt")
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)

#read and readline should not be used at a same time
# we need to write another program

#-----------Writing to a file------
#------------w(it overwrite entire file) or a(adds to the file) mode-----------

# f=open("Day8/08_demo.txt","w")
# f.write("I surpass you")
# f.close()


# f=open("Day8/08_demo.txt","a")
# f.write("\nYou are good Observer.")
# f.close()

#if you do this this will automatically create a new file if not existed

# f=open("Day8/08_sample.txt","a")
# f.close()

# f=open("Day8/08_demo.txt","r+")
# f.write("abc")
# print(f.read())
# f.close()


# f=open("Day8/08_demo.txt","w+")
# # print(f.read())
# f.write("abc")
# f.close()


# f=open("Day8/08_demo.txt","a+")
# print(f.read())
# f.write("abc")
# f.close()


'''r+ read + overwrite (pointer start) - no truncate
   w+ read + overwrite                 -    truncate
   a+ read + append   (pointer end)    -   no truncate
'''


#-----------with syntax-----------
# with open("Day8/08_demo.txt","r") as f:
#     data=f.read()
#     print(data)
#     # f.close() #optional while using with syntax

#--------Deleting a File-------
#using the os module

    #import os
    #os.remove(filename)

# example
import os
# os.remove("Day8/08_demo.txt")

#practice set
 
with open("08_practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java")

with open("Day8/08_practice.txt","r") as f:
    data=f.read()
def replace():
    new_data=data.replace("Java","python")
    print(new_data)
    with open("08_practice.txt","w") as f:
        f.write(new_data)
replace()


def check_for_word(word):
    with open("Day8/08_practice.txt","r") as f:
        data=f.read()
        if(word in data):
            print(word, "exists in the file")
        else:
            print(word,"not exist in the file")

check_for_word("learning")


def check_for_line():
    with open("Day8/08_practice.txt","r") as f:
        word="ok"
        data=True
        line_no=1
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1

    return print(-1)
check_for_line()

count=0
with open("Day8/08_number.txt") as f:
    data=f.read()
    print(data)
    nums=data.split(',') #gives list of string
    print(nums)
    for val in nums:
        if(int(val)%2==0):
            count+=1
print(count)
        
