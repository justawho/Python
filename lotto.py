import random


def lotto():
    number = [0] * 8
    print (number)
    for i in range (7):
        current = random.randint(1, 54)
        print (current)
        while  current not in number:
            number[i] = current
        else:
            current = random.randint(1, 54)
            number[i] = current
    print (number)
    powerball = random.randint(1, 24)
    print ('powerball number: ' + str(powerball))


lotto()
