import re
import numpy as np

def intify(arr):
    return [int(string) for string in arr]

def doubleify(arr):
    return [float(string) for string in arr]

def mix(data):
    originalIndicies = list(range(len(data)))
    length = len(data)
    for index in range(len(data)):
        curIndex = originalIndicies.index(index)
        num = data[curIndex]
        newIndex = (curIndex + num)
        # print('-')
        if newIndex <= 0:
            # print((abs(newIndex) // length))
            newIndex = (newIndex + (-1 * ((abs(newIndex) // length)+1))) % length
        elif newIndex >= length:
            newIndex = (newIndex + (1 * ((abs(newIndex) // length)))) % length
        else:
            notProcessed = False
        data.insert(newIndex, data.pop(curIndex))
        originalIndicies.insert(newIndex, originalIndicies.pop(curIndex))
        # print(data)
    print('working')
    return data

def echo(string):
    print(string)
    return string

if __name__ == '__main__':
    dataFile = open("day202022.txt", "r")
    data = dataFile.read()
    data = data.split('\n')
    data = data[:-1]
    test = ['1', '2', '-3', '3', '-2', '0', '4']
    data = test

    data = [int(string)*811589153 for string in data] # *811589153
    data = mix(data)
    print(data)

    length = len(data)

    zeroPos = data.index(0)
    first = data[(1000+zeroPos) % length]
    second = data[(2000+zeroPos) % length]
    third = data[(3000+zeroPos) % length]

    print(first + second + third)