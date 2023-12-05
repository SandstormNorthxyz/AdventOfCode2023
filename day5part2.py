import copy
import sys

import numpy as np
import pandas as pd
import matplotlib
import re

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

def invDict(dict):
    return {v: k for k, v in dict.items()}

def hashList(list):
    return str(list)

def unHashListInt(string):
    elements = string.replace('[', '').replace(']', '').split(',')
    return [int(element) for element in elements]

def unHashListDouble(string):
    elements = string.replace('[', '').replace(']', '').split(',')
    return [float(element) for element in elements]

if __name__ == '__main__':
    dataFile = open("day5.txt", "r")
    data = dataFile.read()
    data = data.split('\n')
    data = data[:-1]

    runningSum = 0

    seeds = data[0].split(' ')
    seeds.pop(0)
    seeds = [int(string) for string in seeds]
    data.pop(0)

    maps = [{}, {}, {}, {}, {}, {}, {}]

    currentMap = -1

    newRanges = []
    for index, seed in enumerate(seeds):  # knuth forgive me for what i'm about to do
        if index % 2 == 0:
                start = seed
                end = seed + seeds[index+1] - 1
                newRanges.append([start, end])

    checkingRanges = []

    keyNums = []

    for index, dataPoint in enumerate(data):
        print('--------')
        if ':' in dataPoint:
            currentMap += 1
            checkingRanges = newRanges
            newRanges = []
        elif not(dataPoint == ''):
            splits = dataPoint.split(" ")
            splits = [int(string) for string in splits]
            srcStart = splits[1]
            dstStart = splits[0]
            rangeLen = splits[2]
            srcEnd = srcStart + rangeLen - 1
            dstDiff = dstStart - srcStart
            for numRange in checkingRanges:
                start = numRange[0]
                end = numRange[1]
                low = max(srcStart, start)
                high = min(srcEnd, end)
                if low < high:
                    newRanges.append([low + dstDiff, high + dstDiff])
                    keyNums += [low, high]
                # newRanges.append([min(srcStart, low), min(srcEnd, high)])
                # newRanges.append([max(srcStart, low), max(srcEnd, high)])
    print(np.array(newRanges).min())
