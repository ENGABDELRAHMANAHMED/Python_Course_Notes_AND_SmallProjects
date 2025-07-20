##########################
# ---------------------- #
# --- For_Else Loop ---- #
# ---------------------- #
##########################

#################################################
# for   item     in     iterable_object :       #
#          Do Something With Item               #
#################################################

# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]

# Example 1 (List)

myNumbers = [1,2,3,4,5,6,7,8,9]

for number in myNumbers :
    if number %2 ==0 :
        print(f"The Number {number} is an Even Number")
    else :
        print(f"The Number {number} is an Odd Number")
else :
    print("The loop finished")
    
    
myName = "Abdelrahman"

for char in myName :
    print(f"###[{char.upper()}]###")
    
# Example 2 (Range)

myRanges = range(3,14)

for number in myRanges :
    print(number)

# Example 3 (Dictionary)

mySkills = {
  "Html": "90%",
  "Css": "60%",
  "PHP": "70%",
  "JS": "80%",
  "Python": "90%",
  "MySQL": "60%"
}

for skill in mySkills :
    print(f"my progrss in {skill} Language is : {mySkills[skill]}")

# Example 4 (Nested For Loop)

peoples = ["Osama", "Ahmed", "Sayed", "Ali"]
skills = ['Html', 'Css', 'Js']

for name in peoples :
    print(f"{name} skills are : -")
    for skill in skills :
        print(f"- {skill}")
        
        
# Example 5 (Nested For Loop)

SkillProgress = {
  "Osama": {
    "Html": "70%",
    "Css": "80%",
    "Js": "70%"
  },
  "Ahmed": {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  },
  "Sayed": {
    "Html": "70%",
    "Css": "60%",
    "Js": "90%"
  }
}

for name in SkillProgress :
    print(f"Skills and Progress for {name} are :-")
    for skill in SkillProgress[name] :
        print(f"{skill.upper()} ===> {SkillProgress[name][skill]}")
        
##################################
# ------------------------------ #
# --- Break, Continue, Pass ---- #
# ------------------------------ #
##################################


## Example ##

myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# Continue

for number in myNumbers:

  if number == 13:

    continue

  print(number)

print("#" * 50)

# Break

for number in myNumbers:

  if number == 13:

    break

  print(number)

print("#" * 50)

# Pass

for number in myNumbers:

  if number == 13:

    pass

  print(number)
  
  
#####################################
# --------------------------------- #
# --- Advanced Dictionary Loop ---- #
# --------------------------------- #
#####################################

### Example 1 :-

myAdvancedSkills = {
  "HTML": "80%",
  "CSS": "90%",
  "JS": "70%",
  "PHP": "80%",
  "Python": "90%",
  "CCNA": "80%",
  "CCNP": "10%",
  "CCIE": "0%"
}

print(myAdvancedSkills.items())

#First Method
for skill in myAdvancedSkills :
    print(f"{skill} ==> {myAdvancedSkills[skill]}")

#Second Method
for skill_Key , skill_value in myAdvancedSkills.items() :
    print(f"{skill_Key} ==> {skill_value}")


### Example 2 : - 

myUltimateSkills = {
  "HTML": {
    "Main": "80%",
    "Pugjs": "80%"
  },
  "CSS": {
    "Main": "90%",
    "Sass": "70%"
  }
}

for main_key , main_value in myUltimateSkills.items() :
    print(f"{main_key} progress is : ")
    for child_key , child_value in main_value.items() :
          print(f"- {child_key} => {child_value}")