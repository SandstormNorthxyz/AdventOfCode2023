import re
import pandas

if __name__ == '__main__':
    dataFile = open("day2.txt", "r")
    data = dataFile.read()
    data = data.split('\n')
    data = data[:-1]

    colorLims = {'red': 12, 'green': 13, 'blue': 14}

    sum = 0
    powerSum = 0

    for id, game in enumerate(data):
        game = game.split(':')[-1]
        game = game.split(';')
        possible = True
        colorMins = {'red': 0, 'green': 0, 'blue': 0}
        for subset in game:
            colors = subset.split(',')
            for color in colors:
                splits = color.split(' ')
                if int(splits[1]) > colorMins[splits[-1]]:
                    colorMins[splits[-1]] = int(splits[1])
                if int(splits[1]) > colorLims[splits[-1]]:
                    possible = False
        if possible:
            sum += id + 1
        power = colorMins['red'] * colorMins['green'] * colorMins['blue']
        print(colorMins)
        powerSum += power
    print(sum) # part 1
    print(powerSum) # part 2



