# an inventory structure
import csv

inventory = {
            'apples': 2,
            'bananas': 3,
            'limes (lb)': 4,
            'cookies (cases)': 6,
            'sticks of butter': 3
}

def removeInventoryItem(amount, item):
    inventory[item] -= amount
    print(inventory)

def addInventoryItem(amount, item):
    inventory[str(item)] = amount
    if inventory[str(item)] >= 0:
        inventory[item] += amount
    print(inventory)

def writeToFile():
    f = csv.writer(open("inventory.csv", "w"))
    for key, val in inventory.items():
        f.writerow([key, val])

removeInventoryItem(3, 'bananas')
addInventoryItem(5, 'loaves of bread')
writeToFile()
