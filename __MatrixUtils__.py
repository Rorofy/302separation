import time

def matrixPrint(matrix: list):
    t0 = time.time()
    for l in matrix:
        if (time.time() - t0 > 8):
            exit()
        for i in range(len(l)):
            t2 = time.time()
            if i < (len(l) - 1):
                print("{} ".format(l[i]), end='')
            else:
                print(l[i])
            if (time.time() - t2 > 8):
                exit()



def matrixCreate(size: int) -> list:
    return [[0 for _ in range(size)] for _ in range(size)]


def matrixComputeAdjacent(matrix: list, people: list, pairs: list):
    t0 = time.time()
    for duo in pairs:
        matrix[people.index(duo[0])][people.index(duo[1])] = 1
        matrix[people.index(duo[1])][people.index(duo[0])] = 1
        if (time.time() - t0 > 8):
            exit()


def checkFriends(first: int, second: int, inputData) -> bool:
    return inputData.adjacentMatrix[first][second] == 1
