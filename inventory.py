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
    return inventory

def newInventoryItem(amount, item):
    inventory[item] = 0
    if inventory[item] == 0:
        inventory[item] += amount
    return inventory

def increaseInventoryItem(amount,item):
    inventory[item] += amount
    return inventory

def writeToFile():
    f = csv.writer(open("inventory.csv", "w"))
    for key, val in inventory.items():
        f.writerow([key, val])

def readCSVinventory():
    with open('inventory.csv') as f:
        inventory = dict(filter(None, csv.reader(f)))
    print(inventory)

removeInventoryItem(3, 'bananas')
newInventoryItem(5, 'loaves of bread')
increaseInventoryItem(3, 'apples')
writeToFile()
readCSVinventory()