#######################
## ----------------- ##
## --  Decorators -- ##
## ----------------- ##
#######################


# ----------------------------------------------------------------------------------- #
# ## Introduction ## ---------------------------------------------------------------- #
# ----------------------------------------------------------------------------------- #
# [1] Sometimes Called Meta Programming --------------------------------------------- #
# [2] Everything in Python is Object Even Functions --------------------------------- #
# [3] Decorator Take A Function and Add Some Functionality and Return It ------------ #
# [4] Decorator Wrap Other Functions and Enhance Their Behaviour -------------------- #
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter) ---- #
# ----------------------------------------------------------------------------------- #

from time import time


def myDecoratorFunction(functions) : # Decorator
    def myNestedFunction() :  # Any Name Its Just For Decoration
        print("This is Nested Fuction Of The Decorator") # Message From Decorator
        functions()  # Execute Function
    return myNestedFunction # Return All Data

@myDecoratorFunction
def SayHello() :
    print("Hello Abdelrahman Ahmed Khairy")
    
 

@myDecoratorFunction
def SayHowAreYou() :
    print("How are you Abdelrahman Ahmed Khairy ?")
    
    
def SayHowOldAreYou() :
    print("How old are you Abdelrahman Ahmed Khairy ?")
    
myDecoratorVariable = myDecoratorFunction(SayHowOldAreYou)
myDecoratorVariable()
print("#" * 50)   
SayHello()
print("#" * 50)   
SayHowAreYou()
print("#" * 50)   


# -------------------------------- #
# --- Function With Parameters --- #
# -------------------------------- #

def myFirstDecorator(externalFunction):
    def forChecking(*numbers) :
        for number in numbers :
            if number < 0 :
                print("Beware at Least One or more Of the numbers is Less than Zero")
                externalFunction(*numbers)
    return forChecking

def mySecondDecorator(externalFunction):
    def forChecking(*numbers) :
        for number in numbers :
            if number >= 100 :
                print("Beware at Least One or more Of the numbers is Larger than 100 ")
                externalFunction(*numbers)
    return forChecking


@myFirstDecorator
@mySecondDecorator
def calCulator(n1, n2) :
    print(n1 + n2)
    
calCulator(100,-10)


# -------------------------- #
# -- Practical Speed Test -- #
# -------------------------- #


def speedTest(externalFunction):
    def wrapper() :
        start = time()
        externalFunction()
        end = time()
        print(f"The External Function Running Time is {end -start} seconds") 
    return wrapper

@speedTest
def Counter() :
    for number in range(1 , 100000) :
        print(number)
        
Counter()