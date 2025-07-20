##################
##   Training   ##
##################

####################################
## Program for Membership Control ##
####################################

admins =["Abdelrahman Ahmed", "Ahmed Abdelmouty", "Abdelrahman Ezzat", "Ibrahmim Hassan" , "Ahmed Sabry", "Mohammed Amr", "Ayman Sayed", "Abdelrahman Sayed"]

name = input("Please Type your Name ").title().strip()

if name in admins :
    print(f"Hello {name} Welcome Back")
    option = input("Delete or Update your Name (U/D) ").strip().title()
    if option == "Update" or option == "U" :
        TheNewName = input("Your New Name is ").title().strip()
        admins[admins.index(name)] = TheNewName
        print(f"Name Updated. \nYour new name is {TheNewName}")
        print(admins)
    elif option == "Delete" or option == "D" :
        admins.remove(name)
        print(f"Name Deleted. \n {admins}")
    else :
        print("Wrong Option Choosed")
else :
    status = input("Not Admin \nAdd you (Y/N)").strip().title()
    if status == "Y" or status == "Yes" :
        admins.append(name)
        print(f"You Have Been Added \n{admins}")
    else :
        print("You are not Added.")
    