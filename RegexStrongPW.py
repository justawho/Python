### Fnnction that uses regular expressions to make sure the password string is strong
### Strong password being defines as one that is at least eight characters long
### contains both upper and loser case characters and has atleast one digit
import re



def StrongPass(password):
    hasLower = re.compile(r'[a-z]')
    hasUpper = re.compile(r'[[A-Z]')
    hasDigit = re.compile(r'\d')
    
    if len(password) < 8:
        print('This password is too short')
    elif ((hasLower.search(password) and hasUpper.search(password)
    and hasDigit.search(password)) != None):
        print('This is a Strong password')
    elif ((hasLower.search(password) and hasUpper.search(password)
    and hasDigit.search(password)) == None):
        print('This is a weak password')
        
        

print("Please enter a password: ")
password = input()

StrongPass(password)
