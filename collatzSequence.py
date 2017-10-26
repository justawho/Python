def collatz(number):
    if number % 2 == 0:
        newNumber = int(number // 2)
        print (newNumber)
        return int(number // 2)
    else :
        newNumber = (3 * number + 1)
        print (newNumber)
        return int(3 * number + 1)
try:
    print('Please enter an integer.')
    number = int(input())
    while number != 1:
       number = collatz(number)
except ValueError:
    print('Please enter a number') 
        
    
