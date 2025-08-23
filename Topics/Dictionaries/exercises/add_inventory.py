
def displayInventory(inventory):
    print("Inventory")
    
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    print(f"Total number of items: {item_total}")


def addToInventory(inventory, addedItems):
   
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    
    return inventory
        
inv = {
        "rope": 1,
        "gold coin": 42
        }

dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)