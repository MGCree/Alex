import sys
import time
from close import exit
from greetings import greet

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
    while True:
        nameWait = input("Waiting... ")
        cmd = ""

        if nameWait == name:
            while True:
                cmd = input("Waiting on command: ")
                
                if cmd == "exit":
                    exit()                 

                if cmd == "hi":
                    greet()

# Other Variables
startup = True

while startup:
    Startup()
    break
