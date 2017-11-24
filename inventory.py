# inventory.py
# Modeling player inventory with a dictionary.


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


# runs through a users dictionary inventory and dispalys an each item and its quantity followed by the total number of
# items in the inventory.
def displayInventory(inventory):
    print ("Inventory:")
    itemTotal = 0
    for k, v in inventory.items():
        itemTotal = itemTotal + v
        print(str(v) + ' ' + str(k))
    print("Total number of items: " + str(itemTotal))


displayInventory(stuff)


# update inventory numbers or adds items to inventory after looting
def addToInventory(inventory, addedItems):
    for i in set(addedItems):   # iterates through unique list items
        if i in inventory:
            inventory[i] = inventory[i] + addedItems.count(i)   # counts how many times an item is in the list and adds it to the inventory
        else:
            inventory.setdefault(i, addedItems.count(i))     # counts how many times an item is in the list and adds it to the inventory
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
stuff = addToInventory(stuff, dragonLoot)
print('//////////////////////////////////////////////////////////')
print('Inv print out :')
displayInventory(inv)
print('////////////////////////////////////////////////////////////')
print('Stuff print out:')
displayInventory(stuff)
