import random  
def read_items(filename):     
    with open(filename, 'r') as file:         items = file.read().splitlines()     
    return items 
 
def read_wizard_inventory(filename): 
    try:        
         with open(filename, 'r') as file: 
            inventory = file.read().splitlines()     
            except FileNotFoundError: 
        inventory = [] 
    return inventory
 
def write_wizard_inventory(filename, wizard_inventory):     
     with open(filename, 'w') as file: 
        file.write('\n'.join(wizard_inventory)) 
 
def pick(): 
    all_items = read_items('all_items.txt')     
    wizard_inventory = read_wizard_inventory('wizard_inventory.txt') 
 
    items_not_in_inventory = [item for item in all_items if item not in wizard_inventory] 
 
    if len(items_not_in_inventory) == 0: 
        print("You have collected all the items!") 
        return 
 
    random_item = random.choice(items_not_in_inventory)     
    print(f"While walking down a path, you see {random_item}")     
    choice = input("Do you want to graab it? (y/n): ") 
 
    if choice.lower() == 'y':         
        if len(wizard_inventory) < 4: 
            wizard_inventory.append(random_item)             
            write_wizard_inventory('wizard_inventory.txt', wizard_inventory)             
            print(f"You picked up {random_item}") 
        else: 
            print("You can't carry any more items. Drop something first!.") 
    else: 
        print("You chose not to pick up the item.") 
 
pick() 
