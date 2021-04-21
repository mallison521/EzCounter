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

def checkItemCount(item):
    for item in inventory:
        if inventory[item] == 0:
            print(item,": Item is out of stock! Item needs to be restocked!")
            print("------------------------------------------------------------------------")
        elif inventory[item] > 0:
            print(item,": Item in stock! Remaining item count =", inventory[item])
            print("------------------------------------------------------------------------")

item = " "
checkItemCount(item)
removeInventoryItem(3, 'bananas')
addInventoryItem(5, 'loaves of bread')
writeToFile()
