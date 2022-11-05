import os

def createFile():
    fileName = input("Choose a file name:  ")

    file = open(fileName + ".txt", "x")

def deleteFile():
    fileName = input("Choose a file to delete:  ")

    if os.path.exists(fileName + ".txt"):
        os.remove(fileName + ".txt")
    else:
        print("The file does not exist")