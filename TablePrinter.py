## A function named printTable() that rakes a list of lists of strings and
## displays it in a well-organized table


def printTable(someTable):
   colWidths = [0] * len(someTable)
   for j in range (len(someTable[0])):
      for i in range(len(someTable)):
          colWidths[i] = len(max(someTable[i], key=len))
          item =   someTable[i][j]
          print (item.rjust(colWidths[i]), end='' + ' ')
      print('')                 

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
