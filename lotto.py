import random


def lotto():
    number = random.sample(range(1, 69), 5)
    
    powerball = random.randint(1, 24)
    print ((number) ,)
    print ('powerball number: ' + str(powerball))


lotto()

