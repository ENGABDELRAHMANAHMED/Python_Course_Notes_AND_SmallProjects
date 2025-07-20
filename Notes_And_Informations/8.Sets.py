############
# # Sets
############

# [1] Sets Items are Enclosed in curly brackets {}
# [2] Sets are Unordered, Unchangeable, and do not allow duplicate values
# [3] Sets Indexing and Slicing are not possible
# [4] Sets has Only Unique Items    
# [5] Sets has Only Immutable Data Types (e.g., strings, numbers, tuples)
# [6] Sets can be created using the set() constructor or by using curly brackets {}
# [7] Sets can be used to perform mathematical set operations like union, intersection, difference, etc.
# [8] Sets can be iterated over using loops
# [9] Random access to items in a set is not allowed, as sets are unordered collections

myAwesomeSet = {"Abdelrahmn", 24, 3.2, True, ("Muslim", "Egyptian")}
# myAwesomeSet = {"Abdelrahmn", 24, 3.2, True, ["Muslim", "Egyptian"]}  # Raises TypeError: unhashable type: 'list'

print(myAwesomeSet) # Output: {'Abdelrahmn', 24, 3.2, True, ('Muslim', 'Egyptian')}
print(type(myAwesomeSet)) # Output: <class 'set'>
print(len(myAwesomeSet)) # Output: 5

# print(myAwesomeSet[0]) # Raises TypeError: 'set' object is not subscriptable
# print(myAwesomeSet[0:2]) # Raises TypeError: 'set' object is not subscriptable
 

myUniqeItemsSet = {"Hello", "World", 1, 2, "World", "Hello", 5, "Hello", 7, "Hello", 9, 10}
print(myUniqeItemsSet) # Output: {1, 2, 5, 7, 9, 10, 'Hello', 'World'}
# Note that the duplicate items are removed


#######################
## Methods for Sets  ##
#######################

# [1] Clear Method - Removes all items from the set

myUniqeItemsSet.clear()
print(myUniqeItemsSet) # Output: set()

# [2] Copy Method - Returns a shallow copy of the set
myUniqeItemsSet = {"Hello", "World", 1, 2, "World", "Hello", 5, "Hello", 7, "Hello", 9, 10}
myCopySet = myUniqeItemsSet.copy()
myUniqeItemsSet.add("Python")  # Adding an item to the original set
print(myUniqeItemsSet) # Output: {1, 2, 5, 7, 9, 10, 'Hello', 'World'}
print(myCopySet) # Output: {1, 2, 5, 7, 9, 10, 'Hello', 'World'}

# [3] add Method - Adds an item to the set
myUniqeItemsSet.add("Python")
print(myUniqeItemsSet) # Output: {1, 2, 5, 7, 9, 10, 'Hello', 'World', 'Python'}
print(myCopySet)  # Output: {1, 2, 5, 7, 9, 10, 'Hello', 'World'}

# [4] remove Method - Removes the specified item from the set
myUniqeItemsSet.remove("Python")
print(myUniqeItemsSet) # Output: {1, 2, 5, 7, 9, 10, 'Hello', 'World'}
# print(myUniqeItemsSet.remove("JavaScript")) # Raises KeyError: 'JavaScript' if the item is not found in the set

# [5] Union Method - Returns a set that contains all items from both sets
mySet1 = {1, 2, 3}
mySet2 = {3, 4, 5}
mySet3 = {6, 7, 8}

myUnionSet = mySet1.union(mySet2, mySet3)
print(myUnionSet) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(mySet1 | mySet2 | mySet3) # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# [6] Discard Method - Removes the specified item from the set if it exists, does nothing if it doesn't

mySet1.discard("Python")  # Does nothing since "Python" is not in the set
print(mySet1)  # Output: {1, 2, 3}
mySet1.discard(2)  # Removes 2 from the set
print(mySet1)  # Output: {1, 3}

# [7] Pop Method - Removes and returns an arbitrary item from the set

print(mySet1.pop())  # Output: 1 (or 3, depending on the internal order)
print(mySet1.pop())  # Output: 3 (if 1 was popped earlier)
# print(mySet1.pop())  # Raises KeyError: 'pop from an empty set' if the set is empty

# [8] Update Method - Updates the set with items from another set or iterable

mySet1.update(["A", "B", "C"])
mySet1.update(mySet2)
mySet1 |= mySet3
print(mySet1) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 'A', 'B', 'C'}

# [9] Difference Method - Returns a set that contains items in the first set but not in the second set

myCompareSet1 = {1, 2, 3, 4, 5}
myCompareSet2 = {4, 5, 6, 7, 8}
print(myCompareSet1)  # Output: {1, 2, 3, 4, 5}
print(myCompareSet1.difference(myCompareSet2))  # Output: {1, 2, 3}
print(myCompareSet1 - myCompareSet2)  # Output: {1, 2, 3}
print(myCompareSet1) # Output: {1, 2, 3, 4, 5} 

# [10] Difference Update Method - Removes items from the first set that are present in the second set

myCompareSet4 = {10, 20, 30, 40, 50}
myCompareSet5 = {40, 50, 60, 70, 80}
print(myCompareSet4)  # Output: {10, 20, 30, 40, 50}
myCompareSet4.difference_update(myCompareSet5) # Output: None (the method modifies the set in place)
myCompareSet4 -= myCompareSet5 # Output: None (the operator modifies the set in place)
print(myCompareSet4) # Output: {10, 20, 30}

# [11] Symmetric Difference Method - Returns a set that contains items that are in either of the sets but not in both

myCompareSet6 = {100, 200, 300, 400, 500}
myCompareSet7 = {400, 500, 600, 700, 800}
print(myCompareSet6) # Output: {100, 200, 300, 400, 500}
print(myCompareSet6.symmetric_difference(myCompareSet7)) # Output : {100, 200, 300, 600, 700, 800}
print(myCompareSet6 ^ myCompareSet7)  # Output: {100, 200, 300, 600, 700, 800}
print(myCompareSet6) # Output: {100, 200, 300, 400, 500}  # Original set remains unchanged

# [12] Symmetric Difference Update Method - Updates the first set with items that are in either of the sets but not in both

myCompareSet8 = {1000, 2000, 3000, 4000, 5000}
myCompareSet9 = {4000, 5000, 6000, 7000, 8000}
print(myCompareSet8) # Output: {1000, 2000, 3000, 4000, 5000}

myCompareSet8.symmetric_difference_update(myCompareSet9) # Output: None (the method modifies the set in place)
# OR
myCompareSet8 ^= myCompareSet9 # Output: None (the operator modifies the set in place)

print(myCompareSet8) # Output: {1000, 2000, 3000, 6000, 7000, 8000}

# [13] Intersection Method - Returns a set that contains items that are present in both sets

myCompareSet10 = {111, 222, "Abdo", 444, 555} 
myCompareSet11 = {444, 555, 666, 777, 888}
print(myCompareSet10) # Output: {111, 222, 'Abdo', 444, 555} 

print(myCompareSet10.intersection(myCompareSet11)) # Output: {444, 555}
# OR
print(myCompareSet10 & myCompareSet11) # Output: {444, 555}

print(myCompareSet10) # Output: {111, 222, 'Abdo', 444, 555}

# [14] Intersection Update Method - Removes the items in this set that are not present in other, specified set(s)

myCompareSet15 = {1114, 2322, "Abdelrahman", 4454, 5655} 
myCompareSet16 = {4454, 5655, 666, 777, 888}
print(myCompareSet15) # Output: {1114, 2322, "Abdelrahman", 4454, 5655}

myCompareSet15.intersection_update(myCompareSet16) # Output: None (the method modifies the set in place)
# OR
myCompareSet15 &= myCompareSet16 # Output: None (the method modifies the set in place)

print(myCompareSet15) # Output: {4454, 5655}

# [15] issuperset - Returns whether this set contains another set or not

myCompareSet100 = {10, 100, "Abdo", 1000, 10000} 
myCompareSet200 = {10, 100, 1000}
myCompareSet300 = {10, 100, 1000, 10000, 100000}

print(myCompareSet100.issuperset(myCompareSet200)) # Output: True
# OR 
print(myCompareSet100 >= myCompareSet200) # Output: True
# OR
print(myCompareSet100 > myCompareSet200) # Output: True

print(myCompareSet100.issuperset(myCompareSet300)) # Output: False
print(myCompareSet300.issuperset(myCompareSet100)) # Output: False

# [16] issubset - Returns whether another set contains this set or not

print(myCompareSet100.issuperset(myCompareSet200)) # Output: False
# OR 
print(myCompareSet100 <= myCompareSet200) # Output: False
# OR
print(myCompareSet100 < myCompareSet200) # Output: False

print(myCompareSet100.issubset(myCompareSet300)) # Output: False
print(myCompareSet200.issubset(myCompareSet100)) # Output: True

# [17] isdisjoint -	Returns whether two sets have a intersection or not

print(myCompareSet300.isdisjoint(myCompareSet100)) # Output: False
print(myCompareSet300.isdisjoint(myCompareSet1)) # Output: True
