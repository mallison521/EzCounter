# an inventory structure

inventory = {
            'apples': 2,
            'bananas': 3,
            'limes (lb)': 4,
            'cookies (cases)': 6,
            'sticks of butter': 3
}

def removeInventoryItem(amount,item):
    inventory[item] -= amount
    print(inventory)

removeInventoryItem(3, 'bananas')
