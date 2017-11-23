##inventory.py

##Modeling player inventory with a dictionary. 


stuff = {'rope': 1, 'torch':6, 'gold coin': 42, 'dagger': 1, 'arrow':12}



def displayInventory(inventory):
    print ("Inventory:")
    itemTotal = 0
    for  k, v in inventory.values():
        itemTotal = itemTotal + v
        print( str(v) +' '+ str(k))
    print("Total number of items: " + str(itemTotal))

displayInventory(stuff)

