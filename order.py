import csv

inventory = {}
with open('inventory.csv') as f:
    for line in f:
        (key,val) = line.split(',')
        inventory[key] = int(val)
# Use of ingredients for an order of macaroni and cheese
macaroniCheese = {
    "elbow noodles" : .5,
    "cheddar cheese" : .125,
    "gruyere cheese" : .25,
    "milk" : .2,
    "butter stick" : .25
}

#Usage of ingredients for an order of a peanut butter and jelly sandwich
pbj = {
    "peanut butter" : .2,
    "jelly" : .1,
    "white bread" : .2
}


def checkIngredients(orderName):
    if orderName == "pbj":
        if pbj.get("peanut butter") < inventory['peanut butter'] and pbj.get("jelly") < inventory['jelly'] \
            and pbj.get("white bread") < inventory['white bread']:
            print('you can make a pbj')
        else:
            print('you cant make a pbj')

    elif orderName == "macaroniCheese":
        if macaroniCheese.get("elbow noodles") < inventory['elbow noodles'] and\
            macaroniCheese.get('cheddar cheese') < inventory['cheddar cheese'] and\
                macaroniCheese.get('gruyere cheese') < inventory['gruyere cheese'] and\
                    macaroniCheese.get('milk') < inventory['milk'] and\
                        macaroniCheese.get('butter stick') < inventory['butter stick']:
                            print('you can make mac and cheese')
        else:
            print('you cannot make mac and cheese')
                        
                

print(inventory)
checkIngredients('pbj')
checkIngredients('macaroniCheese')

# kas maybe you can add a way to change the data in the inventory csv based off the order? 
