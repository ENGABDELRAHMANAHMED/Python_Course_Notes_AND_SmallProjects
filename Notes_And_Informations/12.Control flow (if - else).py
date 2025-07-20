###################
## Control Flow ##
##################

######################
### If, Elif, Else ###
###   Nested if    ###
######################

# To Get the User Data
YourName = input("Your name is ").title().strip()
YourCountry = input("Your Country is ").title().strip()
CourseName = input("Your Course is ").strip().title()
isStudent = input("Are you Student ? (Y/N)" ).strip().title()

# The Constant Values
PythonPrice = 100
NetworkingPrice = 250
CyberSecurityPrice = 580
CloudComputingPrice = 420
FrontEndPrice = 130
BackEndPrice = 230

# The If Elif Else and nested if Example
if CourseName == "Python" :
    if YourCountry == "Egypt" or YourCountry == "KSA" or YourCountry == "Kuwait":
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${PythonPrice} \nBecause you are from {YourCountry} and you are a Student, You 'll taken 80% Offer \nThe {CourseName} Course Price is ${PythonPrice * 0.8} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${PythonPrice} \nBecause you are from {YourCountry}, You 'll taken 60% Offer \nThe {CourseName} Course Price is ${PythonPrice * 0.6} Only")
        else : 
            print("!!!!! Not a Logic Answer !!!!!")
    elif YourCountry == "USA" or YourCountry == " France" or YourCountry == "German" :
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${PythonPrice} \nBecause you are from {YourCountry} and you are a Student, You 'll taken 50% Offer \nThe {CourseName} Course Price is ${PythonPrice * 0.5} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${PythonPrice} \nBecause you are from {YourCountry}, You 'll taken 20% Offer \nThe {CourseName} Course Price is ${PythonPrice * 0.2} Only")
        else : 
            print("!!!!! Not a Logic Answer !!!!!")
    else :
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${PythonPrice} \nBecause you are a Student, You 'll taken 50% Offer \nThe {CourseName} Course Price is ${PythonPrice * 0.5} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${PythonPrice}")
        else : 
            print("!!!!! Not a Logic Answer !!!!!") 
elif CourseName == "Networking" :
    if YourCountry == "Egypt" or YourCountry == "KSA" or YourCountry == "Kuwait":
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${NetworkingPrice} \nBecause you are from {YourCountry} and you are a Student, You 'll taken 80% Offer \nThe {CourseName} Course Price is ${NetworkingPrice * 0.8} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${NetworkingPrice} \nBecause you are from {YourCountry}, You 'll taken 60% Offer \nThe {CourseName} Course Price is ${NetworkingPrice * 0.6} Only")
        else : 
            print("!!!!! Not a Logic Answer !!!!!")
    elif YourCountry == "USA" or YourCountry == " France" or YourCountry == "German" :
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${NetworkingPrice} \nBecause you are from {YourCountry} and you are a Student, You 'll taken 50% Offer \nThe {CourseName} Course Price is ${NetworkingPrice * 0.5} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${PythonPrice} \nBecause you are from {YourCountry}, You 'll taken 20% Offer \nThe {CourseName} Course Price is ${NetworkingPrice * 0.2} Only")
        else : 
            print("!!!!! Not a Logic Answer !!!!!")
    else :
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${NetworkingPrice} \nBecause you are a Student, You 'll taken 50% Offer \nThe {CourseName} Course Price is ${NetworkingPrice * 0.5} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${NetworkingPrice}")
        else : 
            print("!!!!! Not a Logic Answer !!!!!") 
elif CourseName == "Cyber Security" :
    if YourCountry == "Egypt" or YourCountry == "KSA" or YourCountry == "Kuwait":
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${CyberSecurityPrice} \nBecause you are from {YourCountry} and you are a Student, You 'll taken 80% Offer \nThe {CourseName} Course Price is ${CyberSecurityPrice * 0.8} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${CyberSecurityPrice} \nBecause you are from {YourCountry}, You 'll taken 60% Offer \nThe {CourseName} Course Price is ${CyberSecurityPrice * 0.6} Only")
        else : 
            print("!!!!! Not a Logic Answer !!!!!")
    elif YourCountry == "USA" or YourCountry == " France" or YourCountry == "German" :
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${CyberSecurityPrice} \nBecause you are from {YourCountry} and you are a Student, You 'll taken 50% Offer \nThe {CourseName} Course Price is ${CyberSecurityPrice * 0.5} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${CyberSecurityPrice} \nBecause you are from {YourCountry}, You 'll taken 20% Offer \nThe {CourseName} Course Price is ${CyberSecurityPrice * 0.2} Only")
        else : 
            print("!!!!! Not a Logic Answer !!!!!")
    else :
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${CyberSecurityPrice} \nBecause you are a Student, You 'll taken 50% Offer \nThe {CourseName} Course Price is ${CyberSecurityPrice * 0.5} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${CyberSecurityPrice}")
        else : 
            print("!!!!! Not a Logic Answer !!!!!")    
elif CourseName == "Cloud Computing" :
    if YourCountry == "Egypt" or YourCountry == "KSA" or YourCountry == "Kuwait":
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${CloudComputingPrice} \nBecause you are from {YourCountry} and you are a Student, You 'll taken 80% Offer \nThe {CourseName} Course Price is ${CloudComputingPrice * 0.8} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${CloudComputingPrice} \nBecause you are from {YourCountry}, You 'll taken 60% Offer \nThe {CourseName} Course Price is ${CloudComputingPrice * 0.6} Only")
        else : 
            print("!!!!! Not a Logic Answer !!!!!")
    elif YourCountry == "USA" or YourCountry == " France" or YourCountry == "German" :
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${CloudComputingPrice} \nBecause you are from {YourCountry} and you are a Student, You 'll taken 50% Offer \nThe {CourseName} Course Price is ${CloudComputingPrice * 0.5} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${CloudComputingPrice} \nBecause you are from {YourCountry}, You 'll taken 20% Offer \nThe {CourseName} Course Price is ${CloudComputingPrice * 0.2} Only")
        else : 
            print("!!!!! Not a Logic Answer !!!!!")
    else :
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${CloudComputingPrice} \nBecause you are a Student, You 'll taken 50% Offer \nThe {CourseName} Course Price is ${CloudComputingPrice * 0.5} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${CloudComputingPrice}")
        else : 
            print("!!!!! Not a Logic Answer !!!!!") 
elif CourseName == "Front End" :
    if YourCountry == "Egypt" or YourCountry == "KSA" or YourCountry == "Kuwait":
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${FrontEndPrice} \nBecause you are from {YourCountry} and you are a Student, You 'll taken 80% Offer \nThe {CourseName} Course Price is ${FrontEndPrice * 0.8} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${FrontEndPrice} \nBecause you are from {YourCountry}, You 'll taken 60% Offer \nThe {CourseName} Course Price is ${FrontEndPrice * 0.6} Only")
        else : 
            print("!!!!! Not a Logic Answer !!!!!")
    elif YourCountry == "USA" or YourCountry == " France" or YourCountry == "German" :
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${FrontEndPrice} \nBecause you are from {YourCountry} and you are a Student, You 'll taken 50% Offer \nThe {CourseName} Course Price is ${FrontEndPrice * 0.5} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${FrontEndPrice} \nBecause you are from {YourCountry}, You 'll taken 20% Offer \nThe {CourseName} Course Price is ${FrontEndPrice * 0.2} Only")
        else : 
            print("!!!!! Not a Logic Answer !!!!!")
    else :
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${FrontEndPrice} \nBecause you are a Student, You 'll taken 50% Offer \nThe {CourseName} Course Price is ${FrontEndPrice * 0.5} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${FrontEndPrice}")
        else : 
            print("!!!!! Not a Logic Answer !!!!!") 
elif CourseName == "Back End" :
    if YourCountry == "Egypt" or YourCountry == "KSA" or YourCountry == "Kuwait":
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${BackEndPrice} \nBecause you are from {YourCountry} and you are a Student, You 'll taken 80% Offer \nThe {CourseName} Course Price is ${BackEndPrice * 0.8} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${BackEndPrice} \nBecause you are from {YourCountry}, You 'll taken 60% Offer \nThe {CourseName} Course Price is ${BackEndPrice * 0.6} Only")
        else : 
            print("!!!!! Not a Logic Answer !!!!!")
    elif YourCountry == "USA" or YourCountry == " France" or YourCountry == "German" :
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${BackEndPrice} \nBecause you are from {YourCountry} and you are a Student, You 'll taken 50% Offer \nThe {CourseName} Course Price is ${BackEndPrice * 0.5} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${BackEndPrice} \nBecause you are from {YourCountry}, You 'll taken 20% Offer \nThe {CourseName} Course Price is ${BackEndPrice * 0.2} Only")
        else : 
            print("!!!!! Not a Logic Answer !!!!!")
    else :
        if isStudent == "Y" or isStudent == "Yes" :
            print(f"Hello {YourName}, The Course Price is ${BackEndPrice} \nBecause you are a Student, You 'll taken 50% Offer \nThe {CourseName} Course Price is ${BackEndPrice * 0.5} Only")
        elif isStudent == "N" or isStudent == "No" :
            print(f"Hello {YourName}, The Course Price is ${BackEndPrice}")
        else : 
            print("!!!!! Not a Logic Answer !!!!!") 
else :
    print("!!!!! Not Found !!!!!")

## Ternary Conditional Operator
# Condition If True | If Condition | Else | Condition If False

isTrue = input(f"\nThe {CourseName} Course duration is 3 Months  \nAre you Ready to take this Course Now ? \n(Y/N)").title().strip()
print("Ok Let\'s Go" if isTrue == "Y" or isTrue == "Yes" else "See You Later")