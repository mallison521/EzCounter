# an inventory structure
import csv
import datetime

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
    now = datetime.datetime.now()

    if item == "elbow noodles":
        if inventory['elbow noodles'] < .5:
            informManager = open("outOfStock.txt", "a")
            informManager.write("elbow noodles\tItem is out of stock! Item needs to be restocked!")
            informManager. write(now.strftime("\t%Y-%m-%d %H:%M:%S"))
            informManager.write("\n")
        else:
            print("elbow noodles \t\t Item in stock! Remaining item count =", inventory['elbow noodles'])

    elif item == "cheddar cheese":
        if inventory['cheddar cheese'] < .125:
            informManager = open("outOfStock.txt", "a")
            informManager.write("cheddar cheese\tItem is out of stock! Item needs to be restocked!")
            informManager. write(now.strftime("\t%Y-%m-%d %H:%M:%S"))
            informManager.write("\n")  
        else:
            print("cheddar cheese \t\t Item in stock! Remaining item count =", inventory['cheddar cheese'])
   
    elif item == "gruyere cheese":
        if inventory['gruyere cheese'] < .25:
            informManager = open("outOfStock.txt", "a")
            informManager.write("gruyere cheese\tItem is out of stock! Item needs to be restocked!")
            informManager. write(now.strftime("\t%Y-%m-%d %H:%M:%S"))
            informManager.write("\n")          
        else:
            print("gruyere cheese \t\t Item in stock! Remaining item count =", inventory['gruyere cheese'])

    elif item == "milk":
        if inventory['milk'] < .2:
            informManager = open("outOfStock.txt", "a")
            informManager.write("milk\t\tItem is out of stock! Item needs to be restocked!")
            informManager. write(now.strftime("\t%Y-%m-%d %H:%M:%S"))
            informManager.write("\n")           
        else:
            print("milk \t\t\t Item in stock! Remaining item count =", inventory['milk'])

    elif item == "butter stick":
        if inventory['butter stick'] < .25:
            informManager = open("outOfStock.txt", "a")
            informManager.write("butter stick\tItem is out of stock! Item needs to be restocked!")
            informManager. write(now.strftime("\t%Y-%m-%d %H:%M:%S"))
            informManager.write("\n")            
        else:
            print("butter stick \t\t Item in stock! Remaining item count =", inventory['butter stick'])

    elif item == "peanut butter":
        if inventory['peanut butter'] < .2:
            informManager = open("outOfStock.txt", "a")
            informManager.write("peanut butter\tItem is out of stock! Item needs to be restocked!")
            informManager. write(now.strftime("\t%Y-%m-%d %H:%M:%S"))
            informManager.write("\n")          
        else:
            print("peanut butter \t\t Item in stock! Remaining item count =", inventory['peanut butter'])

    elif item == "jelly":
        if inventory['jelly'] < .1:
            informManager = open("outOfStock.txt", "a")
            informManager.write("jelly\t\tItem is out of stock! Item needs to be restocked!")
            informManager. write(now.strftime("\t%Y-%m-%d %H:%M:%S"))
            informManager.write("\n")          
        else:
            print("jelly \t\t\t Item in stock! Remaining item count =", inventory['jelly'])

    elif item == "white bread":
        if inventory['white bread'] < .2:
            informManager = open("outOfStock.txt", "a")
            informManager.write("white bread\tItem is out of stock! Item needs to be restocked!")
            informManager. write(now.strftime("\t%Y-%m-%d %H:%M:%S"))
            informManager.write("\n")
            informManager.close()
        else:
            print("white bread \t\t Item in stock! Remaining item count =", inventory['white bread'])

def customerOrder(order):
    order = input("What would you like to order? pbj or macaroniCheese - ")

    if order == "pbj":
        if inventory.get("peanut butter") < .2 or inventory.get("jelly") < .1 or inventory.get("white bread") < .2:
            print ("Sorry, we do not have the proper items in stock to make a pbj")
        else:
            inventory['peanut butter'] -= .2
            inventory['jelly'] -= .1
            inventory['white bread'] -= .2
            print ("enjoy your pbj")
    elif order == "macaroniCheese":
        if inventory.get("elbow noodles") < .5 or inventory.get("cheddar cheese") < .125 or inventory.get("gruyere cheese") < .25 or inventory.get("milk") < .2 or inventory.get("butter stick") < .25:
            print("Sorry, we do not have the proper items in stock to make macaroni cheese")
        else:
            inventory['elbow noodles'] -= .5
            inventory['cheddar cheese'] -= .125
            inventory ['gruyere cheese'] -= .25
            inventory ['milk'] -= .2
            inventory['butter stick'] -= .25
            print("enjoy your macaroni cheese")            
            
            
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
decreaseInventoryItem(3, 'jelly')
increaseInventoryItem(5, 'white bread')

while True:
    order = input("Would you like to add an item to your order? Y/N - ")
    if order == "Y":
        customerOrder(order)
    elif order == "N":
     print("Have a nice day!")
     break

writeToFile()
