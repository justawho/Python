import random


def lotto():
    
    numbers = random.sample(range(1, 69), 5)
    powerball = random.randint(1, 24)
    print (numbers)
    print ('powerball number: ' + str(powerball))


lotto()

