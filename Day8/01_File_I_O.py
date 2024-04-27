#--------File I/O in python---------

# python can be used to perform operations on the file(read and write data)

#  Types of all Files
#1.Text files: .txt,.docx,.log etc.
#2. Binary files: .mp4, .mov, .png, .jpeg etc.

# Open, read and close File
#we have to open a file before reading or writing.


# e.g file_name can be sample.txt , demo.docx etc
# mode can be r (read mode) ,w (write mode)
#mode is set to read mode by default

# f=open("file_name","mode")
# data=f.read()
# f.close()


#example
# f=open("08_demo.txt","r")
# # f=open("08_demo.txt","rt") #same as 23
# data=f.read()
# # data=f.read(5) #read 5 character including space too.
# print(data)
# print(type(data))
# f.close()


#----------Reading a file-----------

# data=f.read() #reads entire file
# data=f.readline() #reads one line at a time
# f=open("08_demo.txt")
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)

#read and readline should not be used at a same time
# we need to write another program

#-----------Writing to a file------
#------------w(it overwrite entire file) or a(adds to the file) mode-----------

# f=open("08_demo.txt","w")
# f.write("I surpass you")
# f.close()


# f=open("08_demo.txt","a")
# f.write("\nYou are good Observer.")
# f.close()

#if you do this this will automatically create a new file if not existed

# f=open("08_sample.txt","a")
# f.close()

# f=open("08_demo.txt","r+")
# f.write("abc")
# print(f.read())
# f.close()


# f=open("08_demo.txt","w+")
# # print(f.read())
# f.write("abc")
# f.close()


# f=open("08_demo.txt","a+")
# print(f.read())
# f.write("abc")
# f.close()


'''r+ read + overwrite (pointer start) - no truncate
   w+ read + overwrite                 -    truncate
   a+ read + append   (pointer end)    -   no truncate
'''


#-----------with syntax-----------
with open("08_demo.txt","r") as f:
    data=f.read()
    print(data)
    # f.close() #optional while using with syntax

#--------Deleting a File-------
#using the os module

    #import os
    #os.remove(filename)

# example
import os
# os.remove("08_demo.txt")

#practice set