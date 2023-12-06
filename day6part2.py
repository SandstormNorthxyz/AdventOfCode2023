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

def intify(arr):
    return [int(string) for string in arr if not (string == '')]

def doubleify(arr):
    return [float(string) for string in arr]

def echo(string):
    print(string)
    return string




if __name__ == '__main__':
    dataFile = open("day6.txt", "r")
    data = dataFile.read()
    data = data.split('\n')
    data = data[:-1]

    runningSum = 0

    time = int(data[0].split(':')[-1].replace(' ', ''))
    distance = int(data[1].split(':')[-1].replace(' ', ''))

    firstSet = True

    # for time, distance in zip(times, distances):
    possibles = 0
    for accel in range(time):
        newDist = (time-accel)*accel
        if newDist > distance:
            possibles += 1
        # if firstSet:
        #     runningSum = possibles
        #     firstSet = False
        # else:
        #     runningSum *= possibles
    print(possibles)


