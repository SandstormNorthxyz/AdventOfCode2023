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

if __name__ == '__main__':
    dataFile = open("day3.txt", "r")
    data = dataFile.read()
    data = data.split('\n')
    data = data[:-1]

    digits = ["0", "1", '2', '3', '4', '5', '6', '7', '8', '9']
    notSyms = ["0", "1", '2', '3', '4', '5', '6', '7', '8', '9', '.']

    numTotals = 0

    numCoords = []
    nums = {}

    for row, dataPoint in enumerate(data):
        num = ""
        numIndicies = []
        for col, char in enumerate(dataPoint):
            if char in digits:
                num += char
                numIndicies.append(col)

                if safeIndex(data, row, col+1) not in digits:
                    isNum = False
                    for index in numIndicies:
                        # print(safeIndex(data, row, index - 1))
                        # print(safeIndex(data, row, index - 1) not in notSyms)
                        if (safeIndex(data, row, index - 1) not in notSyms) or (
                                safeIndex(data, row, index + 1) not in notSyms) or (
                                safeIndex(data, row, index) not in notSyms):
                            isNum = True
                    for index in numIndicies:
                        if (safeIndex(data, row - 1, index - 1) not in notSyms) or (
                                safeIndex(data, row - 1, index + 1) not in notSyms) or (
                                safeIndex(data, row - 1, index) not in notSyms):
                            isNum = True
                    for index in numIndicies:
                        if (safeIndex(data, row + 1, index - 1) not in notSyms) or (
                                safeIndex(data, row + 1, index + 1) not in notSyms) or (
                                safeIndex(data, row + 1, index) not in notSyms):
                            isNum = True

                    if isNum:
                        for index in numIndicies:
                            numCoord = [row, index]
                            numCoords.append(numCoord)
                            nums.update({str(numCoord): int(num)})
                        numTotals += int(num)
                        # print(int(num))


                    num = ""
                    numIndicies = []
            else:
                num = ""
                numIndicies = []
    print(numTotals)

    ratioTotals = 0
    for row, dataPoint in enumerate(data):
        for col, char in enumerate(dataPoint):
            if char == "*":
                adjacents = [[row, col+1], [row, col-1], [row+1, col], [row+1, col+1], [row+1, col-1], [row-1, col], [row-1, col+1], [row-1, col-1]]
                matches = []
                print("---------------")
                print(adjacents)
                for adjacent in adjacents:
                    if adjacent in numCoords:
                        matches.append(nums[str(adjacent)])
                matches = list(dict.fromkeys(matches))
                print(matches)
                if len(matches) == 2:
                    ratioTotals += matches[0] * matches[1]

    print(ratioTotals)



