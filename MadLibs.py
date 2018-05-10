#! python3
# MadLibs.py
# a program that reads in text files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import os


fileLocation = r'C:\Users\mjlesseyhordatt\Documents\GitHub\Python'
os.chdir(fileLocation)

# instantiate the terms
terms = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
# open up the MadLibs file 
madFile = open('MadLibs.txt', 'r+')
madContent = madFile.read()
# Split the string into a list of strings
madContent = madContent.split()
madAnswers = open('MadAnswers.txt', 'w')


# Go through the terms list
for i in range(len(terms)):
        #go through the list of strings that was the file.
        for words in range(len(madContent)):
                # if the terms match replace the word in the list of words with the response.
                if terms[i] == madContent[words]:
                        response = input( 'Enter a ' + terms[i] + ' :')
                        madContent[words]=response
                # Had issues with punctuation so made sure to check for that. 
                elif terms[i]+'.' ==madContent[words]:
                        response = input( 'Enter a ' + terms[i] + ' :')
                        madContent[words] = response + '.'
          

                	
# Put the new list into a a new file

madFinal = madAnswers.write(' '.join(madContent))
print (' '.join(madContent))
madFile.close()	
madAnswers.close()
