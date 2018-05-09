#! python3
# MadLibs.py
# a program that reads in text files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.


import os

# instantiate the terms
terms = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
# open up the MadLibs file 
madFile = open('MadLibs.txt', 'r+')
madContent = madFile.read()

madAnswers = open('MadAnswers.txt', 'w')



for i in range(len(terms)):
        if terms[i] in madContent :
                response = input( 'Enter a ' + terms[i] + ' :')
                madContent.replace(terms[i], response, 1)
                print (madAnswers)
	


madFile.close()	
