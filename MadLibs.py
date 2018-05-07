#! python3
# MadLibs.py
# a program that reads in text files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.


import os


terms = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
madFile = open('MadLibs.txt', r)
madContent = mad.read()

for terms in madContent:
	if terms[i].lower == 'adjective':
		lib = input('Enter an adjective: ')
	else:
		lib = input('Enter a '+ terms[i]+ ':')