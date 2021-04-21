# an inventory structure
import csv

def decreaseInventoryItem(amount, item):
    inventory[item] -= amount
    if inventory[item] <= 0:
        inventory[item] = 0
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
    f = csv.writer(open("inventory.csv", "w", newline=''))
    for key, val in inventory.items():
        f.writerow([key, val])

inventory = {}
with open('inventory.csv') as f:
    for line in f:
        (key,val) = line.split(',')
        inventory[key] = int(val)

