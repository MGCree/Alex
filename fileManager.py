import os
import shutil

def createFile():
    fileName = input("Choose a file name:  ")
    fileExtention = input("Choose a file extention:  ")

    file = open(fileName + fileExtention, "x")

def createFolder():
    folderName = input("Choose a name for the folder:  ")
    os.mkdir(folderName)

def appendFile():
    fileName = input("Select file to edit:  ")
    if os.path.exists(fileName):
        file = open(fileName, "a")
        appendText = input("Text to append:  ")
        file.write(appendText)
        file.save()
        file.close()

def deleteFile():
    fileName = input("Choose a file to delete:  ")

    if os.path.exists(fileName):
        os.remove(fileName)
    else:
        print("The file does not exist")

def deleteFolder():
    folder = input("which folder do you want to delete:  ")
    os.rmdir(folder)

def moveFile():
    file = input("which file:  ")
    filePath = os.path.abspath(file)
    destination = input("where:  ")
    destinationPath = os.path.abspath(destination)

    if not os.path.exists(destinationPath):
        os.makedirs(destinationPath)

    shutil.move(filePath, destination)
