#####################
## Type Conversion ##
#####################


# [1] Convert to String

intNumber = 550 
floatNumber = 10.25
boolValue = True  
print(type(intNumber)) # Output : <class 'int'>
print(type(floatNumber)) # Output : <class 'float'>
print(type(boolValue)) # Output : <class 'bool'>

print(type(str(intNumber))) # Output : <class 'str'>
print(type(str(floatNumber))) # Output : <class 'str'>
print(type(str(boolValue))) # Output : <class 'str'>

# [2] Convert to Tuple

String =  "Abdelrahman"
List = [1, 2, 3, 4, 5]
Set = {"Abdelrahman" , "Ahmed" , "Khairy"}
Dictionary = {"One" : 1 , "Two" : 2 , "Three" : 3}

print(String) # Output : Abdelrahman
print(List) # Output : [1, 2, 3, 4, 5]
print(Set) # Output :  {'Khairy', 'Ahmed', 'Abdelrahman'}
print(Dictionary) # Output : {'One': 1, 'Two': 2, 'Three': 3}

print(tuple(String)) # Output : ('A', 'b', 'd', 'e', 'l', 'r', 'a', 'h', 'm', 'a', 'n')
print(tuple(List)) # Output : (1, 2, 3, 4, 5)
print(tuple(Set)) # Output : ('Khairy', 'Ahmed', 'Abdelrahman')
print(tuple(Dictionary)) # Output :  ('One', 'Two', 'Three')

# [3] Convert to List

String =  "Abdelrahman"
Tuple = (1, 2, 3, 4, 5)
Set = {"Abdelrahman" , "Ahmed" , "Khairy"}
Dictionary = {"One" : 1 , "Two" : 2 , "Three" : 3}

print(String) # Output : Abdelrahman
print(Tuple) # Output : (1, 2, 3, 4, 5)
print(Set) # Output :  {'Abdelrahman', 'Ahmed', 'Khairy'}
print(Dictionary) # Output : {'One': 1, 'Two': 2, 'Three': 3}

print(list(String)) # Output : ['A', 'b', 'd', 'e', 'l', 'r', 'a', 'h', 'm', 'a', 'n']
print(list(Tuple)) # Output : [1, 2, 3, 4, 5]
print(list(Set)) # Output : ['Abdelrahman', 'Ahmed', 'Khairy']
print(list(Dictionary)) # Output :  ['One', 'Two', 'Three']

# [4] Convert to Set

String =  "Abdelrahman"
Tuple = (1, 2, 3, 4, 5)
List = ["Abdelrahman" , "Ahmed" , "Khairy"]
Dictionary = {"One" : 1 , "Two" : 2 , "Three" : 3}

print(String) # Output : Abdelrahman
print(Tuple) # Output : (1, 2, 3, 4, 5)
print(List) # Output :  ['Abdelrahman', 'Ahmed', 'Khairy']
print(Dictionary) # Output : {'One': 1, 'Two': 2, 'Three': 3}

print(set(String)) # Output : {'m', 'n', 'b', 'l', 'r', 'h', 'A', 'd', 'e', 'a'}
print(set(Tuple)) # Output : {1, 2, 3, 4, 5}
print(set(List)) # Output : {'Abdelrahman', 'Khairy', 'Ahmed'}
print(set(Dictionary)) # Output :  {'Three', 'Two', 'One'}

# [5] Convert to Dictionary

## Any Thing which you need to convert to dictionary ,must to be contain key and value

Tuple = (("One",1), ("Two",2), ("Three",3))
List = [["One",1], ["Two",2], ["Three",3]]

print(Tuple) # Output : (('One', 1), ('Two', 2), ('Three', 3))
print(List) # Output :  [['One', 1], ['Two', 2], ['Three', 3]]

print(dict(Tuple)) # Output : {'One': 1, 'Two': 2, 'Three': 3}
print(dict(List)) # Output : {'One': 1, 'Two': 2, 'Three': 3}

