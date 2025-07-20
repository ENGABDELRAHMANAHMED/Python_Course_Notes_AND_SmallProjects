#########################
# --------------------- #
# -- While_Else Loop -- #
# --------------------- #
#########################

#################################################
# while condition_is_true                       #
#   Code Will Run Until Condition Become False  #
#################################################

# Example 1 

a = 20 

while a > 0 :
    print(a)
    a -= 1
print("Loop Ended")

# Example 2

myFriends = ["Abdelrahman", "Abdelmouty", "Ezzat", "Ibrahim", "Sabry", "MohammedAmr","M.Ragab","Abdelhakeem", "M.Khalil", "fathy"]

index = 0 
print("Your Friends are :- \n####################")
while index < len(myFriends) :
    print(f"{str(index+1).zfill(3)}: {myFriends[index]}")
    index += 1
else :
    print("All Friends printed to screen")
    
# Example 3 

myWebsites = []
a = input("How many websites are you have ?\n")
maxWebsites = int(a)

while maxWebsites > 0 :
    WebsitesName = input("Website name Without ( https:// ) and Without ( .com ) \n").strip().lower()
    myWebsites.append(f"http://{WebsitesName}.com")
    maxWebsites -= 1
    print(f"Website added . \n{maxWebsites} Places left")
    print(myWebsites)
else :
    print("Bookmark is full , You Can\'t add more Websites")
    
if len(myWebsites) > 0 :
    myWebsites.sort()
    indexx = 0
    print("All Websites are :- \n####################")
    while indexx < len(myWebsites) :
        print(myWebsites[indexx])
        indexx +=1
    else :
        pass
else : 
    pass

# Example 4 

try_again = 3
mainPassword = input("Create Your New Password :\t")
print("Successful Process :) ")
inputPassword = input("Enter your Password :\t")

while inputPassword != mainPassword : 
    try_again -= 1
    print(f"Wrong Password\n{'Last' if try_again == 0 else try_again} Chance left")
    inputPassword = input("Enter your Password :\t")
    if try_again == 0 : 
        print("All Tries Finished.")
        break
else :
    print("Correct Password")