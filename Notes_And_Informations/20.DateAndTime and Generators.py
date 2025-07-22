##############################
## ------------------------ ##
## --   Date and Time    -- ##
## ------------------------ ##
##############################

import datetime

print(dir(datetime))
print(dir(datetime.datetime))

print(datetime.datetime.now()) # Print The Current Date and Time
print(datetime.datetime.now().year) # Print The Current Year Date
print(datetime.datetime.now().month) # Print The Current Month Date
print(datetime.datetime.now().day) # Print The Current Day Date
print(datetime.datetime.min) # Print Start Date 
print(datetime.datetime.max) # Print End Date 
print(datetime.datetime.now().time()) # Print The Current Time
print(datetime.datetime.now().time().hour) # Print The Current Hour Time
print(datetime.datetime.now().time().minute) # Print The Current Minute Time
print(datetime.datetime.now().time().second) # Print The Current Second Time
print(datetime.time.min) # Print Start Date 
print(datetime.time.max) # Print End Date 
print(datetime.datetime(2001, 10 ,26)) # Print Specific Date
print(datetime.datetime(2001, 10 ,26, 12, 40, 15)) # Print Specific Date and Time

myBirthDay = datetime.datetime(2001, 10, 26)
dateNow = datetime.datetime.now()

print(f"my Birthday is {myBirthDay}")
print(f"The Date Now is {dateNow}")
print(f"I am {int((dateNow - myBirthDay).days/365)} Years Old")


# ---------------------------------- #
# -- Date and Time => Format Date -- #
# ---------------------------------- #

print(myBirthDay.strftime("%a"))
print(myBirthDay.strftime("%A"))
print(myBirthDay.strftime("%b"))
print(myBirthDay.strftime("%B"))
print(myBirthDay.strftime("%c"))
print(myBirthDay.strftime("%d"))
print(myBirthDay.strftime("%y"))
print(myBirthDay.strftime("%Y"))
print(myBirthDay.strftime("%d %B %Y"))
print(myBirthDay.strftime("%d, %B, %Y"))
print(myBirthDay.strftime("%B - %Y"))
print(myBirthDay.strftime("%d/%B/%Y"))
print(myBirthDay.strftime("%d - %B - %Y"))


# ---------------------------------------------------------------------------------------------- #
# -- Iterable vs Iterator ---------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------- #
## Iterable ## --------------------------------------------------------------------------------- #
# [1] Object Contains Data That Can Be Iterated Upon ------------------------------------------- #
# [2] Examples (String, List, Set, Tuple, Dictionary) ------------------------------------------ #
# ---------------------------------------------------------------------------------------------- #
## Iterator ## --------------------------------------------------------------------------------- #
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time ------ #
# [2] You Can Generate Iterator From Iterable When Using iter() Method ------------------------- #
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene -------------------- #
# [4] Gives "StopIteration" If Theres No Next Element ------------------------------------------ #
# ---------------------------------------------------------------------------------------------- #

# Examples for Iterable

myString = "Osama"
myList = [1, 2, 3, 4, 5]
myTuple = (1, "Ahmed", 3, 256, 5)
print ("\n")

for name in myString :
    print(name , end=" ")

print ("\n")

for listat in myList :
    print(listat , end=" ")

print ("\n")

for tuplat in myTuple :
    print(tuplat , end=" ")

print ("\n")

# Examples for Iterators

myNewString = iter(myString)

print(next(myNewString))
print(next(myNewString))
print(next(myNewString))
print(next(myNewString))
print(next(myNewString))

for letter in iter("Elzero"):
    print(letter, end=" ")
        
print ("\n")

for letter in "Elzero":
    print(letter, end=" ")
        
print ("\n")


# ------------------------------------------------------------------------------------ #
# -- Generators ---------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------ #
# [1] Generator is a Function With "yield" Keyword Instead of "return" --------------- #
# [2] It Support Iteration and Return Generator Iterator By Calling "yield" ---------- #
# [3] Generator Function Can Have one or More "yield" -------------------------------- #
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining ------- #
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control -------- #
# ------------------------------------------------------------------------------------ #

def myFunc() :
    yield 1
    yield "Abdelrahman"
    yield "Ahmed"
    yield "Khairy"
    yield 2 
    yield 3
    yield 4
    
myGen = myFunc()

print(next(myGen) , end=" ")
print("Hello From Python")
print(next(myGen) , end=" ")
print(next(myGen) , end=" ")
print(next(myGen))

for gen in myGen :
    print(gen)