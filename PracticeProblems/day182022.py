import numpy as np

def getAdjacents(coords):
    coords = [int(coord) for coord in coords.split(',')]
    coords = np.array(coords)

    adjacentDeltas = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])

    adjacents = []
    for delta in adjacentDeltas:
        adjacents.append(coords + delta)

    return [str(coord[0]) + ',' + str(coord[1]) + ',' + str(coord[2]) for coord in adjacents]

    # print(adjacents)

    # print(str(coords).replace('array([', '').replace('])', ''))

if __name__ == '__main__':
    dataFile = open("practice18.txt", "r")
    data = dataFile.read()
    data = data.split('\n')
    data = data[:-1]

    openSides = []

    for coord in data:
        adjacents = getAdjacents(coord)
        for adjacent in adjacents:
            if adjacent not in data:
                openSides.append(adjacent)
    print(len(openSides))

    # total = 0
    # otherTotal = 0
    # for side in openSides:
    #     if side in data:
    #         otherTotal += 1
    #     else:
    #         total += 1
    # print(otherTotal)
    # print(len(data))