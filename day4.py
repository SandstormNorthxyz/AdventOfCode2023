import copy
import numpy as np
import pandas as pd
import matplotlib

def getManAdjacentIndices(row, col, arr):
    m = len(arr)
    n = len(arr[0])
    adjacent_indices = []
    if row > 0:
        adjacent_indices.append((row - 1, col))
    if row+1 < m:
        adjacent_indices.append((row + 1, col))
    if col > 0:
        adjacent_indices.append((row, col - 1))
    if col+1 < n:
        adjacent_indices.append((row, col + 1))
    return adjacent_indices


def getAdjacentIndicies(x, y, arr):
    position = (x, y)
    adj = []

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, arr.shape[0])  # X bounds
            rangeY = range(0, arr.shape[1])  # Y bounds

            (newX, newY) = (position[0] + dx, position[1] + dy)  # adjacent cell

            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))

    return adj

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

def safeIndex(arr, row, col):
    if row > -1 and row < len(arr):
        slice = arr[row]
        # print(slice)
        if col > -1 and col < len(slice):
            return slice[col]
        else:
            return "."
    else:
        return "."

import re

def getNumTotal(cardMatches, card):
    # print(card)
    total = 1
    matches = cardMatches[card]
    totals = [getNumTotal(cardMatches, card+index+1) for index in range(matches)]
    total += sum(totals)
    return total

if __name__ == '__main__':
    dataFile = open("day4.txt", "r")
    data = dataFile.read()
    data = data.split('\n')
    data = data[:-1]

    runningSum = 0

    cardMatches = {}

    for index, dataPoint in enumerate(data):
        split1 = dataPoint.split(":")
        split2 = split1[-1].split("|")
        table = split2[0].split(' ')
        hand = split2[-1].split(' ')

        intTable = []
        for card in table:
            try:
                intTable.append(int(card))
            except:
                pass

        intHand = []
        for card in hand:
            try:
                intHand.append(int(card))
            except:
                pass

        totalWorth = 0
        matches = 0
        for card in hand:
            if card in table and not (card == " ") and not (card == ''):
                if totalWorth == 0:
                    totalWorth = 1
                else:
                    totalWorth *= 2
                matches += 1
        cardMatches.update({index + 1: matches})
        runningSum += totalWorth
    print(cardMatches) # part 1

    runningCards = 0

    for card in list(cardMatches.keys()):
        print(card)
        # runningCards += 1
        runningCards += getNumTotal(cardMatches, card)
    print(runningCards) # part 2

    # # matchesToProcess = copy.deepcopy(cardMatches)
    # allMatches = list(cardMatches.keys())
    # newMatches = list(cardMatches.keys())
    # processed = False
    # while processed == False:
    #     matchesToProcess = newMatches
    #     newMatches = []
    #     nonZeroProcessed = False
    #     print("hhhhhhhhhhhhhhhhhhh")
    #     for card in matchesToProcess:
    #         print("----------")
    #         print(card)
    #         print(cardMatches[card])
    #         start = card
    #         if not (cardMatches[card] == 0):
    #             nonZeroProcessed = True
    #         for index in range(cardMatches[card]):
    #             print(start+index+1)
    #             newMatches.append(start+index+1)
    #             allMatches.append(start+index+1)
    #     if nonZeroProcessed == False:
    #         processed = True
    # print(len(allMatches))




    # print(runningSum)






