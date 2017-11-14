import random


def lotto():
    number = [0] * 8
    
    for i in range (8):
        current = random.randint(1, 54)
        
        if  current not in number:
            number[i] = current
            
        else:
            current = random.randint(1, 54)
            number[i] = current
    powerball = random.randint(1, 24)
    print ((number) ,)
    print ('powerball number: ' + str(powerball))


lotto()

