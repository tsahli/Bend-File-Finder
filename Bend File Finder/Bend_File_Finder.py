#!python
from io import open
import shutil
import os

while True: 
    try:
        goodListName = raw_input("Enter filename of text files with wanted values: ")
        goodListName = goodListName + ".txt"
        goodListFile = open(goodListName, "rb").read()
        break
    except:
        print("File couldn't be opened!\nYour input is case sensitive.\nThis script needs to be in the same folder as the list of wanted values.\n")

mytext = goodListFile.decode('utf16')
wantedValues = mytext.splitlines()
textExtension = ".txt"
cwd = os.getcwd()
newDirInput = raw_input("Enter name of new folder to create: ")
os.mkdir(cwd + "/" + newDirInput)
newDir = cwd + "/" + newDirInput
newVals = []

for line in wantedValues:
    line = line.replace('"','')
    line = line + textExtension
    newVals.append(line)

while True:
    try:
        folderToSearchName = raw_input("Enter the name of the folder to search: ")
        searchPath = "./" + folderToSearchName
        break
    except:
        print("Directory not found!")

for file in os.listdir(searchPath):
    if file in newVals:
        shutil.copy2(searchPath + "/" + file, newDir)
    else: continue