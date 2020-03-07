import random
import time
from tkinter import *

root = Tk()
theLabel = Label(root,text ="Guess the numbers")
TheNumbers = Label(root, text ="Guess the numbers")

def lotto():

    numbers = sorted(random.sample(range(1, 69), 5))
    numString = ', '.join(map(str,numbers))
    powerball = random.randint(1, 24)
    txtOutput = "White Balls : " + numString + '\n' + 'Powerball : ' + str(powerball)     
    return (txtOutput)


def lottodraw():
    drawnumbers = sorted(random.sample(range(1, 69), 5))
    drawnumString = ', '.join(map(str,drawnumbers))
    drawpowerball = random.randint(1, 24)
    drawtxtOutput = "White Balls : " + drawnumString + '\n' + 'Powerball : ' + str(drawpowerball)
    return (drawtxtOutput)

def theDraw():
    i = 0

    yourPick = lotto()
    TheNumbers.config (text=str(yourPick))
    TheNumbers.pack()
    drawPick = lottodraw()

    print (yourPick)
    theLabel.config(text= "The next statement will be the number of times the while statement ran before a match was made")
    theLabel.pack()
    print ("The next statement will be the number of times the while statement ran before a match was made")
    while yourPick != drawPick:
        drawPick = lottodraw()
        i = i+1

    print ("It took " + str(i) + " draws to hit the numbers picked.")
    theLabel.config(text= "It took " + str(i) + " draws to hit the numbers picked.")
    theLabel.pack()
    print (drawPick)
    return ("It took " + str(i) + " draws to hit the numbers picked.")


theLabel.pack()

#root = Tk()
#theLabel = Label(root,text ="Guess the numbers")

TheNumbers.pack()
theLabel.printButton = Button(root, text = "Get Numbers", command = theDraw).pack()





root.mainloop()
