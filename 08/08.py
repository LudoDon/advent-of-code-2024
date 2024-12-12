import time
from typing import Any, Callable
from itertools import combinations

def executeAndTime(f: Callable[..., Any], *args, **kwargs):
    start = time.perf_counter()
    result = f(*args, **kwargs)
    end = time.perf_counter()
    print('++++++++++++')
    print('duration:')
    print(end - start)
    print('result:')
    print(result)

def readData(filename):
    matrix = []
    antennas = {}
    first = True
    rowNumber = -1
    with open(filename, 'r') as file:
        for line in file:
            rowNumber = rowNumber + 1
            value = line.replace('\n','')
            if first:
                matrixNumberOfColumns = len(value)
            else:
                if matrixNumberOfColumns != len(value):
                    raise Exception
            matrix.append(value)
            for columnNumber in range(len(value)):
                v = value[columnNumber]
                if v != '.':
                    if not v in antennas:
                        antennas[v] = set()
                    antennas[v].add((rowNumber,columnNumber))                
    matrixNumberOfRows = len(matrix)
    return (matrix,matrixNumberOfRows,matrixNumberOfColumns, antennas)

# for debugging (and illustration) purposes, prettify the updated grid
def pretty(r):
    s = ''
    for row in range(matrixNumberOfRows):
        s = s + '\n'
        for col in range(matrixNumberOfColumns):
            s = s + r[row][col]
    return s

def copy(r, emptySetValue:bool):
    result = []
    for row in range(matrixNumberOfRows):
        resultRow = []
        for col in range(matrixNumberOfColumns):
            if emptySetValue:
                resultRow.append(set())
            else:
                resultRow.append(r[row][col])
        result.append(resultRow)
    return result

def isCoordinateValid(i,j):
    return i in range(matrixNumberOfColumns) and j in range(matrixNumberOfRows)

def getAntennaPairs(antennas):
    return combinations(antennas, 2)

def addAntinodesForAntennaType(antennas,antiNodes,matrix,allowAllDistances):
    for ((Pi,Pj),(Qi,Qj)) in getAntennaPairs(antennas):
        for (Ai,Aj) in getAntiNodesForPair(Pi,Pj,Qi,Qj,allowAllDistances):
            antiNodes.add((Ai,Aj))
            matrix[Ai][Aj] = '#'
            print(pretty(matrix))

def sign(x:int):
    if x > 0:
        return 1
    if x == 0:
        return 0
    if x < 0:
        return -1
    
def getAntiNodesForPair(ai,aj,bi,bj,allowAllDistances):
    di = ai - bi
    dj = aj - bj

    N = 0 if allowAllDistances else 1
    while(True if allowAllDistances else N == 1):
        Ai = ai + N * sign(di) * abs(di)
        Aj = aj + N * sign(dj) * abs(dj)
        if isCoordinateValid(Ai,Aj):
            yield (Ai,Aj)
            N = N + 1
        else:
            break

    M = 0 if allowAllDistances else 1
    while(True if allowAllDistances else M == 1):
        Bi = bi - M * sign(di) * abs(di)    
        Bj = bj - M * sign(dj) * abs(dj)
        if isCoordinateValid(Bi,Bj):
            yield (Bi,Bj)
            M = M + 1
        else:
            break
    return

def solvePartI(matrix,antennas):
    antiNodes = set()
    # print(pretty(matrix))
    for antenna in antennas:
        addAntinodesForAntennaType(antennas[antenna],antiNodes,matrix,False)        
    return len(antiNodes)

def solvePartII(matrix,antennas):
    antiNodes = set()
    # print(pretty(matrix))
    for antenna in antennas:
        addAntinodesForAntennaType(antennas[antenna],antiNodes,matrix,True)        
    return len(antiNodes)


(matrix,matrixNumberOfRows,matrixNumberOfColumns, antennas) = readData('08/input.txt')
s = copy(matrix, False)

executeAndTime(solvePartI,s,antennas)
executeAndTime(solvePartII,s,antennas)

