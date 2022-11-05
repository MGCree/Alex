import sys
import time
from close import *
from greetings import *
from calculator import *
from fileManager import *

def commands():
    while True:
        nameWait = input("Waiting... ")
        cmd = ""

        if nameWait == name:
            while True:
                cmd = input("Waiting on command: ")
                
                if cmd == "exit":
                    exit()                 
                elif cmd == "hi":
                    greet()
                elif cmd == "calculate":
                    calc()
                elif cmd == "create text file":
                    createFile()
                elif cmd == "delete text file":
                    deleteFile()
                
                else:
                    print("This is not a valid command yet")
