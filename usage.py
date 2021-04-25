#usage calculator

import csv
import usage.csv
import inventory.csv


inventory = {}
with open('inventory.csv') as f:
    for line in f:
        (key,val) = line.split(',')
        inventory[key] = int(val)


usage = {}
with open('usage.csv') as f:
    for line in f:
        (key,val) = line.split(',')
        inventory[key] = int(val)


def usageDaily(amount, item):
    amountNeeded = inventory[item] - usage[item]
    return amountNeeded
