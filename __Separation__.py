import __Matrix__ as Matrix_
import __Utils__ as Utils_
import __MatrixUtils__ as MU_
from sys import *
import time


class Parser():
    def __init__(self) -> None:
        self.n = 6
        self.p1 = None
        self.p2 = None
        self.people = []
        self.duo = []
        self.adjacent = []
        self.gap = []
        self.matrix = Matrix_.Matrix()

    def argsParse(self):
        if len(argv) == 3:
            self.n = (int(argv[2]))
        else:
            self.p1 = argv[2]
            self.p2 = argv[3]

    def fileParse(self, filename: str) -> int:
        t0 = time.time()
        with open(filename) as file:
            for line in file:
                if " is friends with " not in line:
                    exit(84)
                Utils_.lParse(line, self)
            if (time.time() - t0 > 8):
                exit()
        self.people = Utils_.duplicateRm(self.people)
        self.people.sort()
        return 0

    def matrixSetUp(self):
        self.adjacent = MU_.matrixCreate(len(self.people))
        self.gap = MU_.matrixCreate(len(self.people))
        MU_.matrixComputeAdjacent(self.adjacent, self.people, self.duo)
        self.matrix.getMatrixPath(
            self.adjacent, self.gap, len(
                self.people), self.n)

    def run(self, filename: str) -> None:
        self.argsParse()
        if self.fileParse(filename) == 84:
            exit(84)
        self.matrixSetUp()
        Utils_.printOutput(self)
