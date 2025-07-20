######################
# Strings 
######################

myStringOne = 'This is Single Quotes'
myStringTwo = "\nThis is Double Quotes"
myStringThree = '\nThis is a String with "Double Quotes" inside Single Quotes'
myStringFour = "\nThis is a String with 'Single Quotes' inside Double Quotes"
myStringFive = """\nThis is a String with Triple Quotes.
It can span multiple lines.
You can also use 'Single Quotes' and "Double Quotes" inside it."""
myStringSix = '''\nThis is another String with Triple Quotes.
It can also span multiple lines.
You can use "Double Quotes" and 'Single Quotes' inside it as well.'''


print(myStringOne);print(myStringTwo);print(myStringThree);print(myStringFour);print(myStringFive);print(myStringSix)         


####################
# Strings Indexing
####################

myString = "Hello, World!"

print(myString[0]) # Index 0 => H
print(myString[7]) # Index 7 => W
print(myString[-1]) # Index -1 => ! (last character)
print(myString[-6]) # Index 7 => W

####################
# Strings Slicing
####################

print(myString[:])  # Full Data
print(myString[0::1])  # Full Data
print(myString[::1])  # Full Data
print(myString[0:5])  # Slicing from index 0 to 4 => Hello
print(myString[7:12]) # Slicing from index 7 to 11 => World
print(myString[:5])   # Slicing from start to index 4 => Hello
print(myString[7:])   # Slicing from index 7 to end => World
print(myString[-6:])  # Slicing from index -6 to end => World!
print(myString[0:5:2]) # Slicing from index 0 to 4 with step 2 => Hlo
print(myString[::2])  # Slicing from start to end with step 2 => Hlo ol!
print(myString[::3]) # Slicing from start to end with step 3 => Hl r!
print(myString[::-1]) # Reversing the string => !dlroW ,olleH
print(myString[7::-1]) # Reversing from index 7 to start => W ,olleH

####################
# Strings Methods
####################

# 1st Method 
# strip()  rstrip()   lstrip()

myStringWithSpaces = "   Hello, World!   "
print(myStringWithSpaces.strip()) # Removes spaces from both ends => "Hello, World!"
print(myStringWithSpaces.lstrip()) # Removes spaces from the left end => "Hello, World!   "
print(myStringWithSpaces.rstrip()) # Removes spaces from the right end => "   Hello, World!"

myStringWithHashes = "###Hello, World!###"
print(myStringWithHashes.strip('#'))  # Removes '#' from both ends => "Hello, World!"
print(myStringWithHashes.lstrip('#')) # Removes '#' from the left end => "Hello, World!###"
print(myStringWithHashes.rstrip('#')) # Removes '#' from the right end => "###Hello, World!"

myStringWithOthers = "!@#$#$%^$%$%&%*^Hello, World!#@!%#$^%^&&*%&$%&%@"
print(myStringWithOthers.strip('!@#$%^&*()')) # Removes special characters from both ends => "Hello, World!"
print(myStringWithOthers.lstrip('!@#$%^&*()')) # Removes special characters from the left end => "Hello, World!#@!%#$^%^&&*%&$%&%@"
print(myStringWithOthers.rstrip('!@#$%^&*()')) # Removes special characters from the right end => "!@#$#$%^$%$%&%*^Hello, World!"

# 2nd Method
#title()

myStringWithTitle = "hello, world! this is a test string."
print(myStringWithTitle.title())  # Converts the first character of each word to uppercase => "Hello, World! This Is A Test String."

# 3rd Method
#Capitalize()

myStringWithCapitalize = "hello, world! this is a test string."
print(myStringWithCapitalize.capitalize())  # Converts the first character of the string to uppercase => "Hello, world! this is a test string."

# 4th Method
# zfill()

myStringWithZfill = "42"
print(myStringWithZfill.zfill(5))  # Pads the string with zeros on the left to make it 5 characters long => "00042"

# 5th Method
# upper()  lower()  swapcase()

myStringWithCase = "Hello, World!"
print(myStringWithCase.upper())  # Converts the string to uppercase => "HELLO, WORLD!"
print(myStringWithCase.lower())  # Converts the string to lowercase => "hello, world!"
print(myStringWithCase.swapcase())  # Swaps the case of each character => "hELLO, wORLD!"      

# 6th Method
# split()  rsplit() splitlines() join()

myStringWithSplit = "Hello, World! This is a test string."
print(myStringWithSplit.split())  # Splits the string into a list of words => ['Hello,', 'World!', 'This', 'is', 'a', 'test', 'string.']
print(myStringWithSplit.split(',')) # Splits the string at commas => ['Hello', ' World! This is a test string.']
print(myStringWithSplit.rsplit(' ', 2))  # Splits the string from the right at the last two spaces => ['Hello, World! This is a', 'test', 'string.']

myStringWithSplitLines = "Hello, World!\nThis is a test string.\nHave a nice day!"
print(myStringWithSplitLines.splitlines())  # Splits the string into a list of lines => ['Hello, World!', 'This is a test string.', 'Have a nice day!']             
print(myStringWithSplitLines.splitlines(keepends=True))  # Keeps the newline characters => ['Hello, World!\n', 'This is a test string.\n', 'Have a nice day!']

myStringWithJoin = ['Hello', 'World', 'This', 'is', 'a', 'test', 'string.']
print(' '.join(myStringWithJoin))  # Joins the list into a string with spaces => "Hello World This is a test string."

myStringWithJoinComma = ['Hello', 'World', 'This', 'is', 'a', 'test', 'string.']
print(', '.join(myStringWithJoinComma))  # Joins the list into a string with commas => "Hello, World, This, is, a, test, string."   


# 7th Method
#centre()  ljust()  rjust()

myStringWithCentre = "Hello, World!"
print(myStringWithCentre.center(20))  # Centers the string in a field of width 20 => "    Hello, World!     "
print(myStringWithCentre.center(20, '*'))  # Centers the string with '*' padding => "****Hello, World!****"
print(myStringWithCentre.ljust(20))  # Left-justifies the string in a field of width 20 => "Hello, World!        "
print(myStringWithCentre.ljust(20, '*'))  # Left-justifies the string with '*' padding => "Hello, World!********"
print(myStringWithCentre.rjust(20))  # Right-justifies the string in a field of width 20 => "        Hello, World!"
print(myStringWithCentre.rjust(20, '*'))  # Right-justifies the string with '*' padding => "********Hello, World!"  

# 8th Method
# count() 

myStringWithCount = "Hello, World! Hello, Universe!"
print(myStringWithCount.count('Hello'))  # Counts the occurrences of 'Hello' => 2
print(myStringWithCount.count('o'))  # Counts the occurrences of 'o' => 3
print(myStringWithCount.count('l', 0, 5))  # Counts the occurrences of 'l' in the first 5 characters => 2
print(myStringWithCount.count('l', 5))  # Counts the occurrences of 'l' from index 5 to the end => 3

# 9th Method
# startswith()  endswith()

myStringWithStartsEnds = "Hello, World!"
print(myStringWithStartsEnds.startswith('Hello'))  # Checks if the string starts with 'Hello' => True
print(myStringWithStartsEnds.startswith('World'))  # Checks if the string starts with 'World' => False
print(myStringWithStartsEnds.endswith('!'))  # Checks if the string ends with '!' => True
print(myStringWithStartsEnds.endswith('World'))  # Checks if the string ends with 'World' => False
print(myStringWithStartsEnds.startswith('Hello', 0, 5))  # Checks if the string starts with 'Hello' in the first 5 characters => True
print(myStringWithStartsEnds.endswith('World', 0, 12))  # Checks if the string ends with 'World' in the first 12 characters => False    

# 10th Method
# find()  rfind()  index()  rindex()

myStringWithFind = "Hello, World! Hello, Universe!"
print(myStringWithFind.find('Hello'))  # Finds the first occurrence of 'Hello' => 0
print(myStringWithFind.find('World'))  # Finds the first occurrence of 'World' => 7
print(myStringWithFind.find('Universe'))  # Finds the first occurrence of 'Universe' => 21
print(myStringWithFind.rfind('Hello'))  # Finds the last occurrence of 'Hello' => 14
print(myStringWithFind.rfind('World'))  # Finds the last occurrence of 'World' => 7
print(myStringWithFind.rfind('Universe'))  # Finds the last occurrence of 'Universe' => 21
print(myStringWithFind.find('NotFound'))  # Returns -1 if 'NotFound' is not present
print(myStringWithFind.rfind('NotFound'))  # Returns -1 if 'NotFound' is not present

print(myStringWithFind.index('Hello'))  # Finds the first occurrence of 'Hello' and raises an error if not found => 0
print(myStringWithFind.index('World'))  # Finds the first occurrence of 'World' and raises an error if not found => 7    
print(myStringWithFind.index('Universe'))  # Finds the first occurrence of 'Universe' and raises an error if not found => 21
print(myStringWithFind.rindex('Hello'))  # Finds the last occurrence of 'Hello' and raises an error if not found => 14
print(myStringWithFind.rindex('World'))  # Finds the last occurrence of 'World' and raises an error if not found => 7
print(myStringWithFind.rindex('Universe'))  # Finds the last occurrence of 'Universe' and raises an error if not found => 21
# print(myStringWithFind.index('NotFound'))  # Raises an error if 'NotFound' is not present
# print(myStringWithFind.rindex('NotFound'))  # Raises an error if 'NotFound' is not present


# 11th Method
# replace()

myStringWithReplace = "Hello, World! Hello, Universe!"
print(myStringWithReplace.replace('Hello', 'Hi'))  # Replaces 'Hello' with 'Hi' => "Hi, World! Hi, Universe!"
print(myStringWithReplace.replace('World', 'Earth'))  # Replaces 'World' with 'Earth' => "Hello, Earth! Hello, Universe!"
print(myStringWithReplace.replace('Hello', 'Hi', 1))  # Replaces the first occurrence of 'Hello' with 'Hi' => "Hi, World! Hello, Universe!"
print(myStringWithReplace.replace('Hello', 'Hi', 2))  # Replaces the first two occurrences of 'Hello' with 'Hi' => "Hi, World! Hi, Universe!"
# print(myStringWithReplace.replace('NotFound', 'Hi'))  # Raises an error if 'NotFound' is not present

# 12th Method
# expandtabs()

myStringWithExpandTabs = "Hello,\tWorld!\tThis is a test string."
print(myStringWithExpandTabs.expandtabs(4))  # Replaces tabs with spaces (4 spaces) => "Hello,   World!   This is a test string."
print(myStringWithExpandTabs.expandtabs(8))  # Replaces tabs with spaces (8 spaces) => "Hello,        World!        This is a test string." 
# print(myStringWithExpandTabs.expandtabs(0))  # Raises an error if the tab size is less than or equal to 0

# 13th Method
# isalpha()  isdigit()  isalnum()  isspace()  istitle()  isdecimal()
# islower()  isupper() isnumeric() isidentifier() isprintable() isascii()

myStringWithAlpha = "HelloWorld"
print(myStringWithAlpha.isalpha())  # Checks if all characters are alphabetic => True

myStringWithAlphaNum = "HelloWorld123"
print(myStringWithAlphaNum.isalnum())  # Checks if all characters are alphanumeric => True

myStringWithNotDigit = "12345.55"
myStringWithDigit = "1234555"
print(myStringWithNotDigit.isdigit())  # Checks if all characters are digits => False
print(myStringWithDigit.isdigit())  # Checks if all characters are digits => True

myStringWithSpace = "   "
print(myStringWithSpace.isspace())  # Checks if all characters are whitespace => True

myStringWithTitleCheck = "Hello World"
print(myStringWithTitleCheck.istitle())  # Checks if the string is in title case => True

myStringWithLower = "hello world"
print(myStringWithLower.islower())  # Checks if all characters are lowercase => True

myStringWithUpper = "HELLO WORLD"
print(myStringWithUpper.isupper())  # Checks if all characters are uppercase => True

myStringWithNotNumeric = "12345.55"
myStringWithNumeric = "1234555"
print(myStringWithNotNumeric.isnumeric())  # Checks if all characters are numeric => False (because of the decimal point)
print(myStringWithNumeric.isnumeric())  # Checks if all characters are numeric => True

myStringWithIdentifier = "my_variable"
print(myStringWithIdentifier.isidentifier())  # Checks if the string is a valid identifier => True

myStringWithPrintable = "Hello, World!"
myStringWithNonPrintable = "Hello, \x00World!" 
print(myStringWithPrintable.isprintable())  # Checks if all characters are printable => True
print(myStringWithNonPrintable.isprintable())  # Checks if all characters are printable => False (because of the null character)

myStringWithAscii = "Hello, World!"
myStringWithNonAscii = "Hello, 世界!"
print(myStringWithAscii.isascii())  # Checks if all characters are ASCII => True
print(myStringWithNonAscii.isascii())  # Checks if all characters are ASCII => False (because of the non-ASCII character)

####################
# Strings Formating
####################

###############################
# Strings Formatting Old Way ## 
# %s => String               ##
# %d => Number               ##
#  %f => Float               ##
###############################    
myName = "Abdelrahman"
myAge = 24
myGPA = 3.2

myStringFormatOld = "Hello, my name is %s, Iam %d years old and my GPA is %0.1f"% (myName, myAge, myGPA)
myStringFormatOldMod = "Hello, my name is %s, Iam %d years old and my GPA is %0.3f"% (myName, myAge, myGPA)
myStringFormatOldMod2 = "Hello, my name is %s, Iam %d years old and my GPA is %f"% (myName, myAge, myGPA)
print(myStringFormatOld) # Output: Hello, my name is Abdelrahman, Iam 24 years old and my GPA is 3.2
print(myStringFormatOldMod) # Output: Hello, my name is Abdelrahman, Iam 24 years old and my GPA is 3.200
print(myStringFormatOldMod2) # Output: Hello, my name is Abdelrahman, Iam 24 years old and my GPA is 3.2000000

myStringWithTruncation = "Hello, my name is abdelrahman, Iam 24 years old and my GPA is 3.2"
print("My String with Truncation: %.10s" % myStringWithTruncation)  # Output: My String with Truncation: Hello, my name is
print("My String with Truncation: %.5s" % myStringWithTruncation)  # Output: My String with Truncation: Hello 
print("My String with Truncation: %.3s" % myStringWithTruncation)  # Output: My String with Truncation: Hel


################################
# Strings Formatting New Way  ##
# {:s} => String              ##
# {:d} => Number              ##
# {:f} => Float               ##
################################


myStringFormatNew = "Hello, my name is {:s}, Iam {:d} years old and my GPA is {:0.1f}".format(myName, myAge, myGPA)
myStringFormatNewMod = "Hello, my name is {:s}, Iam {:d} years old and my GPA is {:0.3f}".format(myName, myAge, myGPA)
myStringFormatNewMod2 = "Hello, my name is {:s}, Iam {:d} years old and my GPA is {:f}".format(myName, myAge, myGPA)
print(myStringFormatNew)  # Output: Hello, my name is Abdelrahman, Iam 24 years old and my GPA is 3.2
print(myStringFormatNewMod)  # Output: Hello, my name is Abdelrahman, Iam 24 years old and my GPA is 3.200
print(myStringFormatNewMod2)  # Output: Hello, my name is Abdelrahman, Iam 24 years old and my GPA is 3.2000000 

myStringWithTruncationNew = "Hello, my name is abdelrahman, Iam 24 years old and my GPA is 3.2"
print("My String with Truncation: {:.10s}".format(myStringWithTruncationNew))  # Output: My String with Truncation: Hello, my name is
print("My String with Truncation: {:.5s}".format(myStringWithTruncationNew))  # Output: My String with Truncation: Hello 
print("My String with Truncation: {:.3s}".format(myStringWithTruncationNew))  # Output: My String with Truncation: Hel  


# Format Money

myMoney = 1234567.89
print("Foramtted Money is ${:0.2f}".format(myMoney))  # Output: Formatted Money is $1234567.89
print("Foramtted Money is ${:,.2f}".format(myMoney))  # Output: Formatted Money is $1,234,567.89
print("Foramtted Money is ${:,.0f}".format(myMoney))  # Output: Formatted Money is $1,234,568

# Rearranging the String

firstVar , secondVar, thirdVar = "Hello", "World", "Python"
print("Rearranged String: {2} {0} {1}".format(firstVar, secondVar, thirdVar))  # Output: Rearranged String: Python Hello World
print("Rearranged String: {1} {2} {0}".format(firstVar, secondVar, thirdVar))  # Output: Rearranged String: World Python Hello
print("Rearranged String: {0} {2} {1}".format(firstVar, secondVar, thirdVar))  # Output: Rearranged String: Hello Python World

Var1, Var2, Var3 = 1, 2, 3
print("Rearranged String: {2:d} {0:f} {1:d}".format(Var1, Var2, Var3))  # Output: Rearranged String: 3 1 2
print("Rearranged String: {1} {2} {0}".format(Var1, Var2, Var3))  # Output: Rearranged String: 2 3 1
print("Rearranged String: {0} {2} {1}".format(Var1, Var2, Var3))  # Output: Rearranged String: 1 3 2    


# Formatting with f-strings (Python 3.6+)

myStringFormatF = f"Hello, my name is {myName}, Iam {myAge} years old and my GPA is {myGPA:.1f}"
myStringFormatFMod = f"Hello, my name is {myName}, Iam {myAge} years old and my GPA is {myGPA:.3f}"
myStringFormatFMod2 = f"Hello, my name is {myName}, Iam {myAge} years old and my GPA is {myGPA:f}"
print(myStringFormatF)  # Output: Hello, my name is Abdelrahman, Iam 24 years old and my GPA is 3.2
print(myStringFormatFMod)  # Output: Hello, my name is Abdelrahman, Iam 24 years old and my GPA is 3.200
print(myStringFormatFMod2)  # Output: Hello, my name is Abdelrahman, Iam 24 years old and my GPA is 3.2000000

myStringWithTruncationF = "Hello, my name is abdelrahman, Iam 24 years old and my GPA is 3.2"
print(f"My String with Truncation: {myStringWithTruncationF:.10s}")  # Output: My String with Truncation: Hello, my name is
print(f"My String with Truncation: {myStringWithTruncationF:.5s}")  # Output: My String with Truncation: Hello 
print(f"My String with Truncation: {myStringWithTruncationF:.3s}")  # Output: My String with Truncation: Hel    



