import sys
import time
from commandManager import *

#---------Bot Setup----------|
name = "Alex"               #|
creator = "Jakub Jankowski" #|
#----------------------------|

#-----User Info-----|
user = "mgcree"    #|
passcode = "11823" #|
#-------------------|

#Functions
def Startup():
    userCheck = input("Enter your username: ")
    passCheck = input("Enter your passcode: ")

    if userCheck == user and passCheck == passcode:
        main()
    
    elif userCheck != user:
        print ("Wrong username")
    
    elif passCheck != passcode:
        print("Wrong passcode")   

def main():
    print("Welcome Sir")
    commands()

# Other Variables
startup = True

while startup:
    Startup()
    break
