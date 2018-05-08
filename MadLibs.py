#! python3
# MadLibs.py
# a program that reads in text files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.


import os


terms = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
madFile = open('MadLibs.txt', 'r')
madContent = madFile.readlines()
madAnswers = open('MadAnswers.txt', 'w')
response = input('Enter a thing: ')


for i in terms:
        if i in madContent and (i == 'ADJECTIVE' or i =='ADVERB'):
                response = input('Enter an '+ i + ':')
        elif i in madContent and i != 'ADJECTIVE':
                response = input('Enter a ' + i + ':')
	


madFile.close()	
