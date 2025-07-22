##############################
## ------------------------ ##
## --      Modules       -- ##
## ------------------------ ##
##############################

# -------------------------------------------------------- #
# ------------------- Built in Modules ------------------- #
# -------------------------------------------------------- #
# [1] Module is A File Contain A Set Of Functions -------- #
# [2] You Can Import Module in Your App To Help You ------ #
# [3] You Can Import Multiple Modules -------------------- #
# [4] You Can Create Your Own Modules -------------------- #
# [5] Modules Saves Your Time ---------------------------- #
# -------------------------------------------------------- #



import random # Import main Module
from random import random, randint # Import One Or Two Functions From Module 
print(random) # Show the modules details ( Name and path )
print(dir(random)) # Show All Functions Inside Module
print(f"Random Float Number : {random()}")
print(f"Random Integer Number : {randint(100, 200)}")


# ----------------------------------- #
# ------- Create your Modules ------- #
# ----------------------------------- #

import sys # Sys ia a built in function 
print(sys.path) # Show all Paths those are The system can import modules from them
sys.path.append(r"D:\GitANDGithub_Material\Python_Course_Notes_AND_SmallProjects") # to add a different Path from The System paths 

#################################################################
# To Prevent any error ##########################################
# Press ( CTRL + Shift + P ) ####################################
# Search for Settings.json ######################################
# Print The Next Line After PythonPath ##########################
# "python.analysis.extraPaths": [ Write the path Here ] #########
#################################################################
 

import AbdelrahmanModule
print(dir(AbdelrahmanModule))

AbdelrahmanModule.SayHello("Ahmed")
AbdelrahmanModule.SayHello("Osama")
AbdelrahmanModule.SayHello("Mohamed")

AbdelrahmanModule.SayHowAreYou("Ahmed")
AbdelrahmanModule.SayHowAreYou("Osama")
AbdelrahmanModule.SayHowAreYou("Mohamed")

AbdelrahmanModule.SayHowOldAreYou("Ahmed")
AbdelrahmanModule.SayHowOldAreYou("Osama")
AbdelrahmanModule.SayHowOldAreYou("Mohamed")

# Alias the Module Name

import AbdelrahmanModule as AAKMHE
print(dir(AAKMHE))

AAKMHE.SayHello("Ahmed")
AAKMHE.SayHello("Osama")
AAKMHE.SayHello("Mohamed")

AAKMHE.SayHowAreYou("Ahmed")
AAKMHE.SayHowAreYou("Osama")
AAKMHE.SayHowAreYou("Mohamed")

AAKMHE.SayHowOldAreYou("Ahmed")
AAKMHE.SayHowOldAreYou("Osama")
AAKMHE.SayHowOldAreYou("Mohamed")

# Import One Or Two Functions From Module 

import AbdelrahmanModule
print(dir(AbdelrahmanModule))
from AbdelrahmanModule import SayHello, SayHowAreYou

SayHello("Abdelrahman")
SayHowAreYou("Abdrlrahman")

# Import One Or Two Functions From Module With Alias

import AbdelrahmanModule
print(dir(AbdelrahmanModule))
from AbdelrahmanModule import SayHello as SH, SayHowAreYou as SHSHAY

SH("Abdelrahman")
SHSHAY("Abdelrahman")


# ---------------------------------------------------------------------------------------------------------------------------------------------------- #
# ------- Install External Packages ------------------------------------------------------------------------------------------------------------------ #
# ---------------------------------------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------------------------------------------------------------------------------- #
# [1] Module Vs Package ------------------------------------------------------------------------------------------------------------------------------ #
# Module ia a file have any number of functions ------------------------------------------------------------------------------------------------------ #
# Package is a folder have any number of Modules ----------------------------------------------------------------------------------------------------- #
# [2] External Packages Downloaded From The Internet ------------------------------------------------------------------------------------------------- #
# [3] You Can Install Packages With Python Package Manager PIP --------------------------------------------------------------------------------------- #
# [4] PIP Install the Package and Its Dependencies --------------------------------------------------------------------------------------------------- #
# [5] Modules List "https://docs.python.org/3/py-modindex.html" -------------------------------------------------------------------------------------- #
# [6] Packages and Modules Directory "https://pypi.org/" --------------------------------------------------------------------------------------------- #
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/" ------------------------------------------------------------------------------ #
# ---------------------------------------------------------------------------------------------------------------------------------------------------- #
# To Check if you have PIP Or no Should be write (PIP --version) in VSCode Terminal ------------------------------------------------------------------ #
# To show all Installed packages Should be write (PIP list) in VSCode Terminal ----------------------------------------------------------------------- #
# To Install any Package Should be write (PIP Install "The Package Name") in VSCode Terminal --------------------------------------------------------- #
# To Update any Library ( Package Or Group of Packages ) Should be write (PIP install "The Package or Library Name" -- update) in VSCode Terminal ---- #
# ---------------------------------------------------------------------------------------------------------------------------------------------------- #

import termcolor
import pyfiglet 

print(pyfiglet.figlet_format("ENG / Abdelrahman Ahmed "))
print(termcolor.colored(pyfiglet.figlet_format("ENG / Abdelrahman Ahmed") , color="red"))