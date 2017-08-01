stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# this part of the code shows your current inventory


def displayInventory(inventory):
    print("Inventory")
    itemTotal = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        itemTotal = itemTotal + v
    print('Total number of items: ' + str(itemTotal))
# this launches the function that displays current inventory
displayInventory(stuff)


print('')

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


# This is the function that adds the new loot list to the inventory
def addToInventory(inventory, addedItems):
    print('Now your inventory has: ')
    for item in addedItems:
        stuff[item] = stuff.get(item, 0) + 1

# this calls the function that adds the loot to the inventory
addToInventory(stuff, dragonLoot)
# this displays the updated inventory
displayInventory(stuff)
