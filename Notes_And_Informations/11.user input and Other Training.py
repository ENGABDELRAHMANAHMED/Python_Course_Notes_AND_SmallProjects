################
## User Input ##
################

fName = input('What\'s your first name ? ')
mName = input('What\'s your middle name ? ')
lName = input('What\'s your last name ? ')

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print (f"Hello {fName} {mName} {lName} Happy to see You ")

#############################
# Practical Slice of Email ##
#############################

TheName = input('Write your name please:----------- ').capitalize().strip()
TheEmail = input('Write your Email please:----------- ').lower().strip()

TheUserName = TheEmail[:TheEmail.index('@')]
TheWebSite = TheEmail[TheEmail.index('@')+1 :]

print(f"Hello {TheName} your email is {TheEmail} , Your Username is {TheUserName} and your website is {TheWebSite}")

#####################################
## Practical Your Age Full Details ##
#####################################

TheAge = int(input("Your age is : -------- ").strip())

Months = TheAge * 12 
Weeks = Months * 4
Days = TheAge * 365.5
Hours = Days * 24
Minutes = Hours * 60
Seconds = Minutes * 60

print(f"Your age in Years is {int(TheAge)} Year")
print(f"Your age in Months is {int(Months)} Month")
print(f"Your age in Days is {int(Days)} Day")
print(f"Your age in Hours is {int(Hours)} Hour")
print(f"Your age in Minutes is {int(Minutes)} Minute")
print(f"Your age in Seconds is {int(Seconds)} Second")
