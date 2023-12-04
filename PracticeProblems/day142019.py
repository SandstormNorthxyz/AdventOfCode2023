import re
import numpy as np
import pandas as pd
import matplotlib

def extractKeys(string):
    alphaRemoved = re.sub("[^0-9]", "", string)
    num = int(alphaRemoved)

    numRemoved = re.sub(r"\d+", "", string).replace(" ", "")

    return [numRemoved, num]

def lazyAdd(dict, key, num):
    if key in dict:
        dict[key] += num
    else:
        dict[key] = num

if __name__ == '__main__':
    dataFile = open("day142019.txt", "r")
    data = dataFile.read()
    data = data.split('\n')
    data = data[:-1]

    recipes = []

    for dataPoint in data:
        split1 = dataPoint.split('=>')
        result = extractKeys(split1[-1])
        resourcesNeeded = {extractKeys(string)[0]: extractKeys(string)[-1] for string in split1[0].split(",")}
        recipes.append([result[0], result[1], resourcesNeeded])

    oreRecipe = [recipe for recipe in recipes if recipe[0] == 'FUEL'][0]
    # print(oreRecipe)

    totalOre = 0
    finished = False
    # while not finished:
    #     remainingSolve = {}
    test = {}
    print(test)





