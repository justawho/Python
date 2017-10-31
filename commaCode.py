def comma(someList):
    output =''
    for i in range((len(someList) -1)):
        output += someList[i] + ', '
    output += 'and ' + someList[-1]
    print (output)

spam = ['apples', 'bananas', 'tofu', 'cats']
comma(spam)
food = ['Pizza','pasta', 'spaghetti', 'cheese', 'apples', 'bananas', 'tofu', 'cats', 'dogs', 'snails']
comma(food)
