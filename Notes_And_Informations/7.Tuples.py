############
##  Tuples 
############

# [1] Tuple Items are Enclosed in Parentheses
# [2] You can Remove the Parentheses 
# [3] Tuples are Ordered, Unchangeable, and Allow Duplicates
# [4] Tuple are Immutable (Cannot be changed after creation)
# [5] Tuple items is not Unique
# [6] Tuple can contain different data types
# [7] Operators used in Strings and Lists can also be used with Tuples
# [8] Tuple can be created with the tuple() constructor




myAwesomeTupleOne = (1, 2, 3, 4, 5, "Hello", True, 3.14, [6, 7.5, 8])
myAwesomeTupleTwo = 1, 2, 3, 4, 5, "Hello", True, 3.14, [6, 7.5, 8]  # Removing parentheses

# [1] Accessing Tuple Items
print(myAwesomeTupleOne)  # Output: (1, 2, 3, 4, 5, 'Hello', True, 3.14, [6, 7.5, 8])
print(myAwesomeTupleTwo)  # Output: (1, 2, 3, 4, 5, 'Hello', True, 3.14, [6, 7.5, 8])
print(type(myAwesomeTupleOne))  # Output: <class 'tuple'>
print(type(myAwesomeTupleTwo))  # Output: <class 'tuple'>
print(len(myAwesomeTupleOne))  # Output: 9 (length of the tuple)
print(len(myAwesomeTupleTwo))  # Output: 9 (length of the tuple)
print(myAwesomeTupleOne[0])  # Output: 1
print(myAwesomeTupleOne[5])  # Output: Hello
print(myAwesomeTupleOne[-1])  # Output: [6, 7.5, 8]
print(myAwesomeTupleOne[8][1])  # Output: 7.5 (accessing nested list)
print(myAwesomeTupleOne[-3])  # Output: True (accessing with negative index)
print(myAwesomeTupleOne[2:5])  # Output: (3, 4, 5) (slicing the tuple)
print(myAwesomeTupleOne[:3])  # Output: (1, 2, 3) (slicing from start to index 2)
print(myAwesomeTupleOne[3:])  # Output: (4, 5, 'Hello', True, 3.14, [6, 7.5, 8]) (slicing from index 3 to end)
print(myAwesomeTupleOne[::2])  # Output: (1, 3, 5, True, [6, 7.5, 8]) (slicing with step of 2)

# [2] Modifying Tuple Items

# myAwesomeTupleOne[0] = 'One'  # This will raise an error because tuples are immutable
# TypeError: 'tuple' object does not support item assignment
# myAwesomeTupleOne[5] = "World"  # This will also raise an error
# TypeError: 'tuple' object does not support item assignment

myAwesomeTupleOne = myAwesomeTupleOne[:5] + ("World","Abdelrahman") + myAwesomeTupleOne[6:]  # Changing the sixth item
# Note: We create a new tuple by slicing and concatenating
print(myAwesomeTupleOne)  # Output: (1, 2, 3, 4, 5, 'World','Abdelrahman', True, 3.14, [6, 7.5, 8])

# [3] Tuple With Single Item

mySingleItemTupleOne = (42,)  # Note the comma, otherwise it's not a tuple
mySingleItemTupleTwo = 42,  # Also a tuple with a single item
print(mySingleItemTupleOne)  # Output: (42,)
print(mySingleItemTupleTwo)  # Output: (42,)
print(type(mySingleItemTupleOne))  # Output: <class 'tuple'>
print(type(mySingleItemTupleTwo))  # Output: <class 'tuple'>
print(len(mySingleItemTupleOne))  # Output: 1
print(len(mySingleItemTupleTwo))  # Output: 1

# [4] Tuple, List and String Repeat (*)

myTuple = (1, 2, 3)
myList = [1, 2, 3]
myString = "Hello"

print(myTuple * 2)  # Output: (1, 2, 3, 1, 2, 3) (tuple repeated)
print(myList * 2)  # Output: [1, 2, 3, 1, 2, 3] (list repeated)
print(myString * 2)  # Output: HelloHello (string repeated)

#######################
## Methods for Tuple ##
#######################

# [1] Count Method

myAwesomeTupleCount = (1, 2, 3, 4, 5, "Hello", True, 3.14, [6, 7.5, 8], "Hello", "Hello")
print(myAwesomeTupleCount.count("Hello"))  # Output: 3 (count occurrences of "Hello")

# [2] Index Method

print(myAwesomeTupleCount.index("Hello"))  # Output: 5 (index of the first occurrence of "Hello")
print("The First Position of Hello at index {}".format(myAwesomeTupleCount.index("Hello")))  # Output: The First Position of Hello at index 5
print(f"The First Position of 3.14 at index {myAwesomeTupleCount.index(3.14)}")  # Output: The First Position of 3.14 at index 7

# [3] Tuple Destrust # (Unpacking)

myTupleToUnpackOne = (1, 2, 3, "Hello", True)

a, b, c, d, e = myTupleToUnpackOne  # Unpacking the tuple into variables
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: Hello
print(e)  # Output: True

g, h, _, j, k = myTupleToUnpackOne # Unpacking the tuple into variables
print(g)  # Output: 1
print(h)  # Output: 2
print(j)  # Output: Hello
print(k)  # Output: True
# Note: The underscore (_) is often used to ignore a value in unpacking


