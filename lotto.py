import random
from tkinter import *

def lotto():
    
    numbers = sorted(random.sample(range(1, 69), 5))
    numString = ', '.join(map(str,numbers))
    powerball = random.randint(1, 24)
    txtOutput = "White Balls are: " + numString + ' Powerball number: ' + str(powerball) 
    print(txtOutput)






root = Tk()


theLabel = Label(root)
theLabel.printButton = Button(root, text = "Get Numbers", command = lambda:lotto())
theLabel.printButton.pack()

root.mainloop()


