## A function named printTable() that rakes a list of lists of strings and
## displays it in a well-organized table



tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(someTable):
   colWidths = [0] * len(someTable)
   for i in range (len(someTable)):
      colWidths[i] = len(max(someTable[i]))
      for j in range(len(someTable[i])):
          print (len(someTable[i][j]))
          item =   someTable[i][j]
          print (item.rjust(colWidths[i]+1))

        

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


printTable(tableData)
