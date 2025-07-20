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
print(os.path.dirname(os.path.abspath(__file__)))  # Directory For The Opened File
os.chdir(os.path.dirname(os.path.abspath(__file__))) # Change Current Working Directory
print(os.getcwd()) # ( getcwd ) Get Main Current working directory

Current_working_directory = os.getcwd()
file = open(rf"{Current_working_directory}\7.Tuples.py")
print(file)


# -------------------------------- #
# -- File Handling => Read File -- #
# -------------------------------- #

myfile = open("D:\WWE_2K22\WWE 2K22\steam_appid.txt" , "r")
print(myfile)
print(myfile.name)
print(myfile.mode)
print(myfile.encoding)