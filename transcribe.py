import os

def createFile():
    fileName = input("Choose a file name:  ")

    file = open(fileName + ".txt", "w")