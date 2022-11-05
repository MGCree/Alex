import os

def createFile():
    fileName = input("Choose a file name:  ")
    fileExtention = input("Choose a file extention:  ")

    file = open(fileName + fileExtention, "x")

def deleteFile():
    fileName = input("Choose a file to delete:  ")

    if os.path.exists(fileName):
        os.remove(fileName)
    else:
        print("The file does not exist")