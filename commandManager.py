import sys
import time

from close import *
from greetings import *
from calculator import *
from fileManager import *
from webManager import *

#---------Bot Setup----------|
name = "Alex"               #|
creator = "Jakub Jankowski" #|
#----------------------------|

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
                elif cmd == "create file":
                    createFile()
                elif cmd == "delete file":
                    deleteFile()
                elif cmd == "append to file":
                    appendFile()
                elif cmd == "search":
                    openWebPage()
                elif cmd == "create folder":
                    createFolder()
                
                else:
                    print("This is not a valid command yet")
