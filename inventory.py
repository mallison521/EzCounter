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
    for i in range(0,2):
        if i%2 == True:
            f = csv.writer(open("inventoryOld.csv", "w", newline=''))
        else:
            f = csv.writer(open("inventoryNew.csv", "w", newline=''))
        for key, val in inventory.items():
            f.writerow([key, val])
            


def checkItemCount(item):
    if item == "elbow noodles":
        if inventory['elbow noodles'] == 0:
            print("elbow noodles \t\t Item is out of stock! Item needs to be restocked!")
        else:
            print("elbow noodles \t\t Item in stock! Remaining item count =", inventory['elbow noodles'])
    elif item == "cheddar cheese":
        if inventory['cheddar cheese'] == 0:
            print("cheddar cheese \t\t Item is out of stock! Item needs to be restocked!")
        else:
            print("cheddar cheese \t\t Item in stock! Remaining item count =", inventory['cheddar cheese'])
    elif item == "gruyere cheese":
        if inventory['gruyere cheese'] == 0:
            print("gruyere cheese \t\t Item is out of stock! Item needs to be restocked!")
        else:
            print("gruyere cheese \t\t Item in stock! Remaining item count =", inventory['gruyere cheese'])
    elif item == "milk":
        if inventory['milk'] == 0:
            print("milk \t\t\t Item is out of stock! Item needs to be restocked!")
        else:
            print("milk \t\t\t Item in stock! Remaining item count =", inventory['milk'])
    elif item == "butter stick":
        if inventory['butter stick'] == 0:
            print("butter stick \t\t Item is out of stock! Item needs to be restocked!")
        else:
            print("butter stick \t\t Item in stock! Remaining item count =", inventory['butter stick'])
    elif item == "peanut butter":
        if inventory['peanut butter'] == 0:
            print("peanut butter \t\t Item is out of stock! Item needs to be restocked!")
        else:
            print("peanut butter \t\t Item in stock! Remaining item count =", inventory['peanut butter'])
    elif item == "jelly":
        if inventory['jelly'] == 0:
            print("jelly \t\t\t Item is out of stock! Item needs to be restocked!")
        else:
            print("jelly \t\t\t Item in stock! Remaining item count =", inventory['jelly'])
    elif item == "white bread":
        if inventory['white bread'] == 0:
            print("white bread \t\t Item is out of stock! Item needs to be restocked!")
        else:
            print("white bread \t\t Item in stock! Remaining item count =", inventory['white bread'])
            
inventory = {}
with open('inventory.csv') as f:
    for line in f:
        (key,val) = line.split(',')
        inventory[key] = int(val)
 
checkItemCount('elbow noodles')
checkItemCount('cheddar cheese')
checkItemCount('gruyere cheese')
checkItemCount('milk')
checkItemCount('butter stick')
checkItemCount('peanut butter')
checkItemCount('jelly')
checkItemCount('white bread')
decreaseInventoryItem(3, 'elbow noodles')
increaseInventoryItem(5, 'white bread')
writeToFile()
