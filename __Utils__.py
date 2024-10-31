from sys import *
import __MatrixUtils__ as MU_


def lParse(line: str, inputData) -> None:
    line = line.replace('\n', '')
    first, second = line.replace(" is friends with ", ";").split(';')
    inputData.people.append(first)
    inputData.people.append(second)
    inputData.duo.append([first, second])


def duplicateRm(elem: list) -> list:
    return list(set(elem))


def printOutput(inputData):
    if inputData.p1 is not None and inputData.p2 is not None:
        print(
            "Degree of separation between {} and {}: ".format(
                inputData.p1, inputData.p2), end='')
        if inputData.p1 not in inputData.people or inputData.p2 not in inputData.people:
            print("-1")
        else:
            first = inputData.people.index(inputData.p1)
            second = inputData.people.index(inputData.p2)
            print(inputData.gap[first][second])
    else:
        [print(person) for person in inputData.people]
        print()
        MU_.matrixPrint(inputData.adjacent)
        print()
        MU_.matrixPrint(inputData.gap)
