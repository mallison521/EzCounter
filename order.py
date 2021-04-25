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
        if pbj.get("peanut butter") < inventory[0] and pbj.get("jelly") < inventory[1] and pbj.get("white bread") < inventory[2]
            return True

    elif orderName == "macaroniCheese":
        if macaroniCheese.get("elbow noodles")

