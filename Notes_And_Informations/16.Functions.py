##########################
# ---------------------- #
# ----   Functions  ---- #
# ---------------------- #
##########################

# [1] A Function is A Reusable Block Of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY ( Don't Reapeat Yourself )
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
# [9] A Function Is For All Team and All Apps

#####################
## Simple Examples ##
#####################

# 1 #

def simpleFunction1() :
  print("Hello this is my first function")
  
  
simpleFunction1()

# 2 #

def simpleFunction2() :
  return "Hello this is my first function"
  
print(simpleFunction2())

# 3 #

def simpleFunction3() :
  return "Hello this is my first function"
  
dataFromFunction = simpleFunction3()
print(dataFromFunction)

# 4 #

def say_hello(name):
  print(f"Hello Mr {name}")

say_hello("Abdelrahman Ahmed Khairy")
#################################################################################
## def                                        => Function Keyword [Define]     ##
## say_hello()                                => Function Name                 ##
## name                                       => Parameter                     ##
## print(f"Hello Mr {name}")                  => Task                          ##
## say_hello("Abdelrahman Ahmed Khairy")      => Ahmed is The Argument         ##
#################################################################################

# 5 #

def addition(num1 , num2) :
  print(num1 + num2)
  
addition(200 , 500)


##############
## Examples ##
##############

# [1]

def addition2(num3 , num4) :
  if type(int(num3)) != int or type(int(num4)) != int :
     print("Only interger numbers allowed")
  else :
    print(int(num3) + int(num4))
    
addition2( 500 , "5000")

# [2]

def full_name(first, middle, last):
  print(f"Hello {first.strip().title()} {middle.strip().title()} {middle.strip().title()}")

full_name("abdELRahman     " , "aHMEd" , "kHAIRy")



# --------------------------------- #
# -- Function Default Parameters -- #
# --------------------------------- #

def default_function(name = " Unknown" , age = "unknown" , country = "unknown") :
  
  print(f"## Your name is {name} \nYour age is {age} \nYour Country is {country} ##")
  

default_function("Osama", 36, "Egypt")
default_function("Mahmoud", 28, "KSA")
default_function("Sameh", 38)
default_function("Ramy")
default_function()



# --------------------------------------------------- #
# -- Function Packing, Unpacking Arguments (*Args) -- #
# --------------------------------------------------- #
  
# Simple Say Hello Program with a specific number of peoples

def sayHello(name1 , name2 , name3 ,name4) :
  peoples =[name1 , name2 , name3 , name4]
  for name in peoples :
    print(f"Hello {name} ")
    
sayHello("Abdelarman" , "Ahmed" , "Khairy" , "Mahmoud" )
    
# Simple Say Hello Program with infinite number of peoples

def sayHello(*peoples) : 
  for name in peoples :
    print(f"Hello {name} ")
  
sayHello("Abdelarman" , "Ahmed" , "Khairy" , "Mahmoud" ,"Abdelarman" , "Ahmed" , "Khairy" , "Mahmoud" ,"Abdelarman" , "Ahmed" , "Khairy" , "Mahmoud" )

# Example #

def showSkills(name , *skills) :
  print(f"Hello {name} your skills are :=- ")
  for skill in skills :
    print(f"## {skill} ##")

showSkills("Osama", "Html", "CSS", "JS")
showSkills("Ahmed", "Html", "CSS", "JS", "Python", "PHP", "MySQL")



# ------------------------------------------------------ #
# -- Function Packing, Unpacking Arguments (**KWArgs) -- #
# --------- (**Args) are using with dictionary --------- #
# ------------------------------------------------------ # 

## Simple Example ##

mySkills = {
  'Html': "80%",
  'Css': "70%",
  'Js': "50%",
  'Python': "80%",
  "Go": "40%"
}

def showSkillsExample(name , **myExampleSkills ) :
  print(f"Hello {name} your skills are :=- ")
  for skill_key , skill_value in myExampleSkills.items() :
    print(f"## {skill_key}  +======>  {skill_value} ")

showSkillsExample("Abdelrahman" , **mySkills)


# ----------------------------------------------------- #
# -- Function Packing, Unpacking Arguments Trainings -- #
# ----------------------------------------------------- #

myTuple = ("Go", "Python", "MySQL")

mySkills = {
  'Go': "80%",
  'Python': "50%",
  'MySQL': "80%"
}

def show_skills(name, *skills, **skillsWithProgres):
    print(f"Hello {name} ## :) ## \nSkills without progress are :=- ")
    for singleArg in skills :
      print(f"## {singleArg} ##")
    
    print("and your skills with progress are :=- ")
    for doubleArg_Key , doubleArg_Value in skillsWithProgres.items() :
      print(f"## {doubleArg_Key}  +======>  {doubleArg_Value} ")

show_skills("Abdelrahman" , *myTuple , **mySkills)



# -------------------- #
# -- Function Scope -- #
# -------------------- #


x = 1  # Global Scope

def one():
  global x # Global Scope
  x = 2 # Function Scope
  print(f"Print Variable From Function Scope {x}")

def two():
  x = 10 # Function Scope
  print(f"Print Variable From Function Scope {x}")

one()
print(f"Print Variable From Global Scope {x}")
two()
print(f"Print Variable From Global Scope After One Function Is Called {x}")




# --------------------------- #
# --  Recursion Functions  -- #
# --------------------------- #


# --------------------------------------------------------------------- #
# -- To Understand Recursion, You Need to First Understand Recursion -- #
# --------------------------------------------------------------------- #


def cleanWord(word) :
    if len(word) == 1 :
        return word 
    if word[0] == word[1] :
        return cleanWord(word[1:])
    return word[0] + cleanWord(word[1:])

print(cleanWord("WWWWOOORRRRRRRLLLLLLLLDDDDDDDDDD".lower().strip()))


# ------------------------ #
# -- Function => lambda -- #
# -- Anonymous Function -- #
# ------------------------ #


# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function



# Normal Function 

def say_hello(name, age) :
    return f"Hello {name} your Age Is: {age}"

print(say_hello("Ahmed", 36))
print(say_hello.__name__)


# Lambda Function 

sayHello = lambda Yourname , Yourage : f"Hello {Yourname} your age is {Yourage} "

print(sayHello("Ahmed", 36))
print(sayHello.__name__)
print(type(sayHello))