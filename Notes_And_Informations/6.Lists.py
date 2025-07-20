############
# # Lists 
############

# [1] List Items are Enclosed in Square Brackets
# [2] Lists are Ordered, Changeable, and Allow Duplicates
# [3] Lists are Mutable (add or remove items)
# [4] Lists can contain different data types
# [5] Lists can be nested (lists within lists)
# [6] Lists can be sliced and indexed
# [7] List Items is not Unique
# [8] Lists can be iterated over using loops
# [9] Lists can be concatenated and repeated

myAwesomeList = [1, 2, 3, 4, 5, "Hello", True, 3.14, [6, 7.5, 8]]

# [1] Accessing List Items
print(myAwesomeList)  # Output: [1, 2, 3, 4, 5, 'Hello', True, 3.14, [6, 7, 8]]
print(myAwesomeList[0])  # Output: 1
print(myAwesomeList[5])  # Output: Hello
print(myAwesomeList[-1])  # Output: [6, 7, 8]
print(myAwesomeList[8][1])  # Output: 7 (accessing nested list)
print(myAwesomeList[-3]) # Output: True (accessing with negative index)
print(myAwesomeList[2:5])  # Output: [3, 4, 5] (slicing the list)
print(myAwesomeList[:3])  # Output: [1, 2, 3] (slicing from start to index 2)
print(myAwesomeList[3:])  # Output: [4, 5, 'Hello', True, 3.14, [6, 7.5, 8]] (slicing from index 3 to end)
print(myAwesomeList[::2]) # Output: [1, 3, 5, True, 8] (slicing with step of 2)


# [2] Modifying List Items
print(myAwesomeList)  # Output: [1, 2, 3, 4, 5, 'Hello', True, 3.14, [6, 7.5, 8]]
myAwesomeList[0] = 10  # Changing the first item
myAwesomeList[5] = "World"  # Changing the sixth item
myAwesomeList[1:4] = [200] # Changing a slice of items
print(myAwesomeList)  # Output: [10, 200, 5, 'World', True, 3.14, [6, 7.5, 8]]
myAwesomeList[6:7] = [] # Removing the item at index 6
print(myAwesomeList)  # Output: [10, 200, 5, 'World', True, 3.14]  

#######################
## Methods for Lists ##
#######################

# [1] Append Method

myNewCairoFriends = ["Mahmoud", "Ragab", "Omar"]
myOldFriends = ["Abdelmouty", "Ezzat", "Ibrahim"]
myChildFriends = ["Ahmed", "Mohamed", "Ali"]

myNewCairoFriends.append("Abdelhakeem")  # Adding a new friend
print(myNewCairoFriends)  # Output: ['Mahmoud', 'Ragab', 'Omar', 'Abdelhakeem']

myNewCairoFriends.append(myOldFriends)  # Adding a list of old friends
print(myNewCairoFriends)  # Output: ['Mahmoud', 'Ragab', 'Omar', 'Abdelhakeem', ['Abdelmouty', 'Ezzat', 'Ibrahim']] 
print(myNewCairoFriends[4][1]) # Output: Ezzat (accessing nested list)

# [2] Extend Method

myNewCairoFriends.extend(myChildFriends)  # Adding a list of child friends
myNewCairoFriends.extend(["Hassan", "Khaled"])  # Adding multiple items
myNewCairoFriends.extend(myOldFriends)  # Adding another list
print(myNewCairoFriends)  # Output: ['Mahmoud', 'Ragab', 'Omar', 'Abdelhakeem', ['Abdelmouty', 'Ezzat', 'Ibrahim'], 'Ahmed', 'Mohamed', 'Ali', 'Hassan', 'Khaled', 'Abdelmouty', 'Ezzat', 'Ibrahim']        

# [3] Remove Method

myNewCairoFriends.remove("Hassan")  # Removing a specific item
myNewCairoFriends.remove(myNewCairoFriends[4])  # Removing a nested list
print(myNewCairoFriends)  # Output: ['Mahmoud', 'Ragab', 'Omar', 'Abdelhakeem', 'Ahmed', 'Mohamed', 'Ali', 'Khaled', 'Abdelmouty', 'Ezzat', 'Ibrahim']

# [4] Sort Method

myNewCairoFriends.sort()  # Sorting the list in ascending order
print(myNewCairoFriends)  # Output: ['Abdelhakeem', 'Abdelmouty', 'Ahmed', 'Ali', 'Ezzat', 'Ibrahim', 'Khaled', 'Mahmoud', 'Mohamed', 'Omar', 'Ragab']
myNewCairoFriends.sort(reverse=True)  # Sorting the list in descending order
print(myNewCairoFriends)  # Output: ['Ragab', 'Omar', 'Mohamed', 'Mahmoud', 'Khaled', 'Ibrahim', 'Ezzat', 'Ali', 'Ahmed', 'Abdelmouty', 'Abdelhakeem']      

# [5] Reverse Method

myOldFriends.reverse()  # Reversing the order of the list
print(myOldFriends)  # Output: ['Ibrahim', 'Ezzat', 'Abdelmouty']

# [6] Clear Method

myChildFriends.clear()  # Clearing the list
print(myChildFriends)  # Output: []

# [7] Copy Method

NewList = myOldFriends.copy()  # Creating a copy of the list
print(myOldFriends) # Output: ['Ibrahim', 'Ezzat', 'Abdelmouty']
print(NewList)  # Output: ['Ibrahim', 'Ezzat', 'Abdelmouty']    

myOldFriends.append("Atef")  # Adding a new item to the original list
print(myOldFriends)  # Output: ['Ibrahim', 'Ezzat', 'Abdelmouty', 'Atef']
print(NewList)  # Output: ['Ibrahim', 'Ezzat', 'Abdelmouty'] (the copy remains unchanged)

# [8] Count Method

NewList.append("Ibrahim")  # Adding an item to the copied list
print(NewList.count("Ibrahim"))  # Output: 2 (counting occurrences of 'Ibrahim')

# [9] Index Method

print(NewList.index("Ezzat"))  # Output: 1 (finding the index of 'Ezzat')
print(NewList.index("Ibrahim", 1))  # Output: 3 (finding the index of 'Ibrahim' starting from index 1)  

# [10] Insert Method

NewList.insert(0, "Hossam") # Inserting 'Hossam' at index 0
print(NewList)  # Output: ['Hossam', 'Ibrahim', 'Ezzat', 'Abdelmouty', 'Ibrahim']

# [11] Pop Method

print(NewList.pop())  # Output: 'Ibrahim' (removing and returning the last item)
print(NewList)  # Output: ['Hossam', 'Ibrahim', 'Ezzat', 'Abdelmouty']  # Remaining items after pop     
print(NewList.pop(1))  # Output: 'Ibrahim' (removing and returning the item at index 1)
print(NewList)  # Output: ['Hossam', 'Ezzat', 'Abdelmouty']  # Remaining items after pop at index 1 

