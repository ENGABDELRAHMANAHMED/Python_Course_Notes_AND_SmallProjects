##############################
## ------------------------ ##
## -- Built In Functions -- ##
## ------------------------ ##
##############################

# ------------------------ #
# ------- Part One ------- #
# ------------------------ #
# [01] all() ------------- # 
# [02] any() ------------- #
# [03] bin() ------------- #
# [04] id() -------------- #
# [05] sum() ------------- #
# [06] round() ----------- #
# [07] range() ----------- #
# [08] print() ----------- #
# [09] abs() ------------- #
# [10] pow() ------------- #
# [11] min() ------------- #
# [12] max() ------------- #
# [13] slice() ----------- #
# [14] enumerate() ------- #
# [15] help() ------------ #
# [16] reversed() -------- #
# [17] map() ------------- #
# [18] filter() ---------- #
# [19] reduce() ---------- #
# ------------------------ #


# ---------- #
# [01] all() # 
# ---------- #



TrueAllList = [1, 2, 3, 4, 5]
FalseAllList = [1, 2, 3, 4, 5 , [] ]

print( "All Elements of the list are true" if all(TrueAllList) else "There is at Least One Element is false" )
print( "All Elements of the list are true" if all(FalseAllList) else "There is at Least One Element is false" )

# ---------- #
# [02] any() # 
# ---------- #

TrueAnyList = [1, 2, (), 0, []]
FalseAnyList = [0, False, 0, () , [] ]

print( "There is at Least One Element is True" if any(TrueAnyList) else "All Elements of the list are false" )
print( "There is at Least One Element is True" if any(FalseAnyList) else "All Elements of the list are false" )

# ------------------------------------------------ #
# - [03] bin() ----------------------------------- #
# - get the binary number for the Decimal number - #
# ------------------------------------------------ #

print(bin(5))
print(bin(100))

# --------- #
# [04] id() # 
# --------- #

a = 1
b = 2
print(id(a))
print(id(b))

# ------------------------ #
# [05] sum() ------------- # 
# sum(iterable, start) --- #
# ------------------------ #

SumList = [1, 10, 19, 40] # Itearble Object
print(sum(SumList))
print(sum(SumList, 100))

# ---------------------------- #
# [06] round() --------------- # 
# round(number, numOfDigit) -- #
# ---------------------------- #

print(round(150.499))
print(round(150.501))
print(round(150.554, 2))
print(round(150.556, 2))

# ----------------------------- #
# [07] range() ---------------- # 
# range(start, end, step) ----- #
# ----------------------------- #
# Start and Step are Optional - #
# ----------------------------- #

print(list(range(0))) # It's mean from Zero To Zero
print(list(range(10))) # It's mean from Zero To 9
print(list(range(0, 20, 2)))  # It's mean from Zero To 19 (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)

# ------------ #
# [08] print() # 
# ------------ #

print("Hello Osama How Are You")
print("Hello", "Osama", "How", "Are", "You" ,sep=" ") # Default Value Of Separator is Space
print("Hello", "Osama", "How", "Are", "You" ,sep="#")
print("Hello", "Osama", "How", "Are", "You" ,sep="-")

print("First Line ", end="How are You ") # The Default Value Of The End Is \n
print("First Line", end=" ")
print("Second Line")
print("Third Line")

# --------------------------------------------- #
# [09] abs() ---------------------------------- # 
# The Absolute Value -------------------------- #
# is The Distance From Your number And Zero --- #
# --------------------------------------------- #

print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))

# --------------------------------------------- #
# [10] pow() ---------------------------------- # 
# pow(base, exponent, modulus) ---------------- #
# Modulus Only is Optional -------------------- #
# The Power Of Number Value ------------------- #
# --------------------------------------------- #

print(pow(2, 5))  # 2 * 2 * 2 * 2 * 2
print(pow(2, 5, 10))  # (2 * 2 * 2 * 2 * 2) % 10

# --------------------------------------------- #
# [11] min() ---------------------------------- # 
# min(Group of Items or iterator) ------------- #
# --------------------------------------------- #

myNumbers = (1, 20, -50, -100, 100)
print(min(1, 10, -50, 20, 30))
print(min("X", "Z", "Osama"))
print(min(myNumbers))

# --------------------------------------------- #
# [12] max() ---------------------------------- # 
# max(Group of Items or iterator) ------------- #
# --------------------------------------------- #

myNumbers = (1, 20, -50, -100, 100)
print(max(1, 10, -50, 20, 30))
print(max("X", "Z", "Osama"))
print(max(myNumbers))

# --------------------------------------------- #
# [13] slice() -------------------------------- # 
# slice(start, end, step) --------------------- #
# Start and Step are Optional ----------------- #
# --------------------------------------------- #

a = ["A", "B", "C", "D", "E", "F"]
print(a[:3])
print(a[slice(3)])
print(a[slice(2, 5)])

# ------------------------------------------------------------ #
# [14] enumerate() ------------------------------------------- # 
# enumerate(iterable, start) --------------------------------- #
# The Default Value Of Start is Zero and It's an Optional ---- #
# ------------------------------------------------------------ #

mySkills = ["Html", "Css", "Js", "PHP"]
mySkillsCounter = enumerate(mySkills, 20)
for counter , skill in mySkillsCounter :
    print(f"{counter}. {skill}")


# -------------- #
# [15] help() -- # 
# -------------- #

print(help(print))

# --------------------- #
# [16] reversed() ----- # 
# reversed(iterable) -- # 
# --------------------- #

myString = "Elzero"
for letter in myString :
    print(letter)
for Rletter in reversed(myString) :
    print(Rletter)
    
    
# ----------------------------------------------------------------- #
# [17] map() ------------------------------------------------------ # 
# 1_ Map Take A Function + Iterator ------------------------------- #
# 2_ Map Called Map Because It Map The Function On Every Element -- #
# 3_ The Function Can Be Pre-Defined Function or Lambda Function -- #
# ----------------------------------------------------------------- #

# Use Map With Predefined Function

myTexts = [" OSama ", "AHMED", "  sAYed  "]

def formatText(text) :
    return f"- {text.strip().title()} -"

formatTextVariable = map(formatText, myTexts)

for name in formatTextVariable :
    print(name)

# Use Map With Lambda Function

for named in map(lambda texted : f"- {texted.title().strip()} -", myTexts) :
    print(named)
    
    
# -------------------------------------------------------------------- #
# [18] filter() ------------------------------------------------------ # 
# 1_ Filter Take A Function + Iterator ------------------------------- #
# 2_ Filter Run A Function On Every Element -------------------------- #
# 3_ The Function Can Be Pre-Defined Function or Lambda Function ----- #
# 4_ Filter Out All Elements For Which The Function Return True ------ #
# 5_ The Function Need To Return Boolean Value ----------------------- #
# -------------------------------------------------------------------- #

# Example 1 (For Numbers)

myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

def CheckNumber(number) :
    return number >= 10

TheCheckResult = filter(CheckNumber, myNumbers)

for number in TheCheckResult :
    print(number)
    
    
# Example 2 (For Names)

myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ameer"]

def CheckName(name) : 
    return name.startswith("O")

CheckNameResult = filter(CheckName, myNames)

for name in CheckNameResult :
    print(name)
    
    
# Example 3 (For Lambda Function)

for person in filter(lambda named : named.startswith("A"), myNames) :
    print(person)


# ------------------------------------------------------------------------ #
# [19] reduce() ---------------------------------------------------------- # 
# 1_ Reduce Take A Function + Iterator ----------------------------------- #
# 2_ Reduce Run A Function On FIrst and Second Element And Give Result --- #
# 3_ Then Run Function On Result And Third Element ----------------------- #
# 4_ Then Run Function On Rsult And Fourth Element And So On ------------- #
# 5_ Till One ELement is Left And This is The Result of The Reduce ------- #
# 6_ The Function Can Be Pre-Defined Function or Lambda Function --------- #
# ------------------------------------------------------------------------ #


from functools import reduce

# Example One

numbers = [1, 8, 2, 9, 100]

def myFunc(num1, num2) :
    return num1 + num2

ReduceVariable = reduce(myFunc, numbers)
print(ReduceVariable)

# Example Two

Result = reduce(lambda num1, num2 : num1 + num2 , numbers)
print(Result)