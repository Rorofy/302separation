import __MatrixUtils__ as MU_
import time

class Matrix():
    def __init__(self):
        self.matrixSize = 0
        self.adjacentMatrix = []
        self.matrixRelation = []

    def gapCompute(
            self,
            origin: int,
            dest: int,
            Gap: int,
            currentPath: list) -> int:
        if origin == dest:
            return Gap
        Gap += 1
        newPath = []
        currentPath.append(origin)
        t0 = time.time()
        for people in range(self.matrixSize):
            if (time.time() - t0 > 8):
                exit()
            if MU_.checkFriends(
                    people, origin, self) and (
                    people not in currentPath):
                newGap = self.gapCompute(
                    people, dest, Gap, currentPath.copy())
                if newGap > 0:
                    newPath.append(newGap)
        if len(newPath) == 0:
            return -1
        return min(newPath)

    def getMatrixPath(
            self,
            adjacent: list,
            matrixRelation: list,
            peopleNb: int,
            maxGap: int) -> None:
        self.matrixSize = peopleNb
        self.adjacentMatrix = adjacent
        self.matrixRelation = matrixRelation
        for i in range(self.matrixSize):
            for j in range(i + 1, self.matrixSize):
                Gap = self.gapCompute(i, j, 0, [])
                if Gap > maxGap:
                    Gap = 0
                elif Gap == -1:
                    Gap = 0
                matrixRelation[i][j] = Gap
                matrixRelation[j][i] = Gap
