import re

if __name__ == '__main__':
    dataFile = open("day1.txt", "r")
    data = dataFile.read()
    data = data.split('\n')
    data = data[:-1]

    replacements = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    # 54265
    sum = 0
    for dataPoint in data:
        for key in replacements.keys():
            dataPoint = dataPoint.replace(key, key + replacements[key] + key)
        removed = re.sub("[^0-9]", "", dataPoint)
        numStr = removed[0] + removed[-1]
        sum += int(numStr)
    print(sum)

    # for dataPoint in data:
    #     nums = []
    #     indices = []
    #
    #     for digit in replacements.keys():
    #         num = replacements[digit]
    #         if digit in dataPoint:
    #             occurrences = [m.start() for m in re.finditer(digit, dataPoint)]
    #             indices += occurrences
    #             nums += [num for _ in occurrences]
    #         if num in dataPoint:
    #             occurrences = [m.start() for m in re.finditer(num, dataPoint)]
    #             indices += occurrences
    #             nums += [num for _ in occurrences]
    #
    #     numList = [num for _,num in sorted(zip(indices, nums))]
    #     numStr = numList[0] + numList[-1]
    #     sum += int(numStr)
    # print(sum)