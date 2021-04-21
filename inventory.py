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


def checkItemCount(item):
    for item in inventory:
        if inventory[item] == 0:
            print(item,": Item is out of stock! Item needs to be restocked!")
            print("------------------------------------------------------------------------")
        elif inventory[item] > 0:
            print(item,": Item in stock! Remaining item count =", inventory[item])
            print("------------------------------------------------------------------------")
            
inventory = {}
with open('inventory.csv') as f:
    for line in f:
        (key,val) = line.split(',')
        inventory[key] = int(val)

item = " "
checkItemCount(item)
removeInventoryItem(3, 'bananas')
addInventoryItem(5, 'loaves of bread')
writeToFile()


