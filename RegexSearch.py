#! python3
## RegexSearch.pw
## A program that opens all .txt files in a folder and searches for any line
## that matches a user supplied regular expression. The result will be
## printed to the screen.

import re, os, glob
from pathlib import Path


def regFinder(fileName, regex):
    userRegex = re.compile((regex), re.I)
    results = userRegex.search(fileName)
    entry = re.split(regex, fileName)
    print (entry)


data_folder = Path("Python/regexSearch")
os.chdir(data_folder)
regex = input("Please enter what you would like to search for: ")

for file in glob.glob('./*.txt'):
    print(file)
    filer = open(file, 'r')
    fileContent = filer.readlines()
    for i in  range(len(fileContent)):
        line = str(i)
        if regex in fileContent[i].lower():
            print ("Input can be found on line: "+ line  )
            print (fileContent[i])
            

            
