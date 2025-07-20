###############
# # Dictionary
###############

# [1] Dict Items are Enclosed in Curly Brackets {}
# [2] Dict Items are Contain {key : value}
# [3] Dict Key need to be Immutable => (Number, String, Tuple) List not allowed
# [4] Dict Value can have any data types
# [5] Dict Key need to be Unique
# [6] Dict is not ordered, you access its element with key

#  Accessing Dict Items

user = {
    "name" : "Abdelrahman",
    "Age" : 24,
    "Country" : "Egypt",
    "Skills" : ["Python" , "Flutter" , "Web development"],
    "GPA" : 3.2,
    "Languages" : {
        "Origin" : {
            "name" : "Arabic",
            "Progress" : "80%"
            },
        "First" : {
            "name" : "English",
            "Progress" : "30%"
            },
        "Second" : {
            "name" : "German",
            "Progress" : "10%"
            }
    }
}

print(user)
print(user["Country"]) # Output : 'Egypt'
print(user.get("Country")) # Output : 'Egypt'

print(user.keys()) # Output : dict_keys(['name', 'Age', 'Country', 'Skills', 'GPA', 'Languages'])
print(user.values()) # Output : dict_values(['Abdelrahman', 24, 'Egypt', ['Python', 'Flutter', 'Web development'], 3.2, {'Origin': {'name': 'Arabic', 'Progress': '80%'}, 'First': {'name': 'English', 'Progress': '30%'}, 'Second': {'name': 'German', 'Progress': '10%'}}])
print(len(user)) # Output : 6
print(len(user["Languages"])) # Output : 3

print(user["Languages"]) # Output : {'Origin': {'name': 'Arabic', 'Progress': '80%'}, 'First': {'name': 'English', 'Progress': '30%'}, 'Second': {'name': 'German', 'Progress': '10%'}}
print(user["Languages"]["Origin"]) # Output : {'name': 'Arabic', 'Progress': '80%'}
print(user["Languages"]["Origin"]["name"]) # Output : Arabic

# Create Dictionary from Variables

myOriginLanguage = {
    "name" : "Arabic",
    "Progress" : "90%",
    "Accent" : "Egyption"
}

myFirstLanguage = {
    "name" : "English",
    "Progress" : "60%",
    "Accent" : "American"
}

mySecondLanguage = {
    "name" : "German",
    "Progress" : "5%",
    "Accent" : "Germany"
}

myLanguages = {
    "Origin" : myOriginLanguage,
    "First" : myFirstLanguage,
    "Second" : mySecondLanguage
}

print(myLanguages) # Output : {'Origin': {'name': 'Arabic', 'Progress': '90%', 'Accent': 'Egyption'}, 'First': {'name': 'English', 'Progress': '60%', 'Accent': 'American'}, 'Second': {'name': 'German', 'Progress': '5%', 'Accent': 'Germany'}}


#######################
## Methods for Dict  ##
#######################

# [1] Clear Method - Removes all the elements from the dictionary

myClearDict = {
    "name" : "Abdelrahmn",
    "Age" : 24 ,
    "GPA" : 3.2
}

print(myClearDict) # Output: {'name': 'Abdelrahmn', 'Age': 24, 'GPA': 3.2}
myClearDict.clear()
print(myClearDict) # Output: {}

# [2] Update Method - Updates the dictionary with the specified key-value pairs 

myUpdateDict = {
    "name" : "Abdelrahmn",
    "Age" : 24 ,
    "GPA" : 3.2
}

print(myUpdateDict) # Output : {'name': 'Abdelrahmn', 'Age': 24, 'GPA': 3.2}
myUpdateDict["Country"] = "Egypt"
print(myUpdateDict) # Output : {'name': 'Abdelrahmn', 'Age': 24, 'GPA': 3.2, 'Country': 'Egypt'}
myUpdateDict.update({"Job" : "Engineer"})
print(myUpdateDict) # Output : {'name': 'Abdelrahmn', 'Age': 24, 'GPA': 3.2, 'Country': 'Egypt', 'Job': 'Engineer'}

# [3] Copy Method - Returns a copy of the dictionary

myCopyDict = {
    "name" : "Abdelrahman",
    "Age" : 24,
    "GPA" : 3.2
}

print(myCopyDict) # Output : {'name': 'Abdelrahmn', 'Age': 24, 'GPA': 3.2}
mypasteDict = myCopyDict.copy()
print(mypasteDict) # Output : {'name': 'Abdelrahmn', 'Age': 24, 'GPA': 3.2}
myCopyDict.update({"Job" : "Engineer"})
print(myCopyDict) # Output : {'name': 'Abdelrahmn', 'Age': 24, 'GPA': 3.2, 'Job': 'Engineer'}
print(mypasteDict) # Output : {'name': 'Abdelrahmn', 'Age': 24, 'GPA': 3.2}


# [4] Key Mehtod - Returns a list containing the dictionary's keys

print(myLanguages.keys()) # Output : dict_keys(['Origin', 'First', 'Second'])

# [5] Value Method - Returns a list of all the values in the dictionary

print(myLanguages.values()) # Output : dict_values([{'name': 'Arabic', 'Progress': '90%', 'Accent': 'Egyption'}, {'name': 'English', 'Progress': '60%', 'Accent': 'American'}, {'name': 'German', 'Progress': '5%', 'Accent': 'Germany'}])

# [6] Form Keys Method - Returns a dictionary with the specified keys and value

Keys = ('myFirstKey', 'mySecondKey', 'myThirdKey')
Values = "Default"

print(dict.fromkeys(Keys, Values)) # Output : {'myFirstKey': 'Default', 'mySecondKey': 'Default', 'myThirdKey': 'Default'}

# [7] Get Method - Returns the value of the specified key

myGettingDict = {
    "myNAme" : "Abdelrahman",
    "Country" : "Egypt"
}

print(myGettingDict.get("Country")) # Output : Egypt

# [8] Items Method - Returns a list containing a tuple for each key value pair Until if you Update in the Origin Dictionary

myItemDict = {
    "name" : "Abdelrahmn",
    "Age" : 24 ,
    "GPA" : 3.2 
}

allItems = myItemDict.items()
myItemDict.update({"Country" : "Egypt"})
print(allItems) # Output : dict_items([('name', 'Abdelrahmn'), ('Age', 24), ('GPA', 3.2), ('Country', 'Egypt')])
#Note => the out put is a Collection of Tuples in One List

# [9] Pop Method - Removes the element with the specified key

myPopDict = {
    "name" : "Abdelrahmn",
    "Age" : 24 ,
    "GPA" : 3.2
}

print(myPopDict.pop("GPA")) # Output : 3.2
print(myPopDict) # Output : {'name': 'Abdelrahmn', 'Age': 24}

# [10] Pop Item Method - Removes the last inserted key-value pair

myPopItemDict = {
    "name" : "Abdelrahmn",
    "Age" : 24 ,
    "GPA" : 3.2
}

print(myPopItemDict)  # Output : {'name': 'Abdelrahmn', 'Age': 24, 'GPA': 3.2}
myPopItemDict.update({"Country" : "Egypt"}) # To update the dictionary because pop item get the last updated value
print(myPopItemDict) # Output : {'name': 'Abdelrahmn', 'Age': 24, 'GPA': 3.2, 'Country': 'Egypt'}
print(myPopItemDict.popitem()) # Output : ('Country', 'Egypt')
print(myPopItemDict) # Output : {'name': 'Abdelrahmn', 'Age': 24, 'GPA': 3.2}


# [11] Set Default Method - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

mySetDefaultDict = {
    "myName" : "Abdelrahman",
}

print(mySetDefaultDict) # Output : {'myName': 'Abdelrahman'}
print(mySetDefaultDict.setdefault("myName")) # will print the value from the dictionary because its exist (Abdelrahman)
print(mySetDefaultDict.setdefault("myAge")) # will print (None) because its not have any value in the dictionary and its not exist
print(mySetDefaultDict) # Output : {'myName': 'Abdelrahman', 'myAge': None}
