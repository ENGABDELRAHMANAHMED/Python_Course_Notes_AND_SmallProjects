#########################
## ------------------- ##
## -- File Handling -- ##
## ------------------- ##
#########################

# ------------------------------------------------------------------------------------- #
# "a" Append  Open File For Appending Values, Create File If Not Exists                 #
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists   #
# "w" Write   Open File For Writing, Create File If Not Exists                          #
# "x" Create  Create File, Give Error If File Exists                                    #
# --------------------------------------------------------------------------------------#


# To reading any absolute path

# ---------------------------------------------------- #
# print("The directory name Such as :- ")              #
# file = open("D:\Courses\Python\Elzero Web School")   #
# ---------------------------------------------------- #

# To reading any relative path 

import os  # ( OS ) Operating System
print(os.getcwd()) # ( getcwd ) Get Main Current working directory
print(os.path.abspath(__file__)) # ( __file__ ) The current file
print(os.path.dirname(__file__))  # Directory For The Opened File
print(os.path.dirname(os.path.abspath(__file__)))  # Directory For The Opened File
os.chdir(os.path.dirname(os.path.abspath(__file__))) # Change Current Working Directory
# os.remove("The Absolute Path") 
print(os.getcwd()) # ( getcwd ) Get Main Current working directory


# -------------------------------- #
# -- File Handling => Read File -- #
# -------------------------------- #

Current_working_directory = os.getcwd()
print(Current_working_directory)
file = open(rf"{Current_working_directory}\7.Tuples.py")
print(file)
print(file.name)
print(file.mode)
print(file.encoding)
print(file.read(450)) # The inside number is the number of the bytes that we need show
print(file.read()) # The Default Value Of read is ( -1 )
print(file.readline()) # Read The first line
print(file.readline()) # Read The Second line
print(file.readline()) # Read The Third line
print(file.readline(5)) # Read 5 bytes only from the first line and move other bytes to the second line 
print(file.readlines()) # Read All Lines as alist
 
# Small Example

for line in file :
    print(line)
    if line.startswith("# [8]") : break

file.close()


# -------------------------------------------- #
# -- File Handling => Write and Append File -- #
# -------------------------------------------- #

# ----------- #
# -- Write -- #
# ----------- #

# in write mode if the file doesn't exist , It Will Be Created
# in write mode delete all file content and write the new content that I write

myList = ["Ahmed\n" , "Abdelrahman\n" , "Khairy\n"]
NewFile = open(r"D:\Courses\Python\Elzero Web School\test.txt" , "w")
NewFile.write("This is my First training in write mode \n")
NewFile.write("This is my Second training in write mode \n")
NewFile.write("This is my Third training in write mode \n")
NewFile.write("#" * 1000 +"\n")
NewFile.writelines(myList)

# ------------ #
# -- Append -- #
# ------------ #

# in Apped mode doesn't delete any line in the content 
NewFile = open(r"D:\Courses\Python\Elzero Web School\test.txt" , "a")
NewFile.write("This is my First training in write mode \n")
NewFile.write("This is my Second training in write mode \n")
NewFile.write("This is my Third training in write mode \n")


# --------------------------------------------- #
# --- File Handling => Import informatiomns --- #
# --------------------------------------------- #

# -------------- #
# -- Truncate -- #
# -------------- #

NewFile = open(r"D:\Courses\Python\Elzero Web School\test.txt" , "a")
NewFile.truncate(5) 

# ---------- #
# -- Tell -- #
# ---------- #

NewFile = open(r"D:\Courses\Python\Elzero Web School\test.txt" , "a")
print(NewFile.tell())

# ---------- #
# -- Seek -- #
# ---------- #

NewFile = open(r"D:\Courses\Python\Elzero Web School\test.txt" , "r")
NewFile.seek(11)
print(NewFile.read())

