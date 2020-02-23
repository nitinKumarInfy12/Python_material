stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    print("Inventory: ")
    total = 0
    for k,v in inventory.items():
        print(f"{v} {k}")
        total = total + v
    print(f"Total number of items : {total}")
    print("======================================================")

#display_inventory(stuff)


def addToInventory(inventory, addedItems):
    for i in addedItems:
        v = inventory.setdefault(i,0) + 1
        inventory[i] = v
    return inventory

display_inventory(stuff)
inv = addToInventory(stuff,dragonLoot)
display_inventory(stuff)
