import re

def readData(filename):
    r = []
    first = True
    with open(filename, 'r') as file:
        for line in file:
            value = line.replace('\n','')
            if first:
                matrixNumberOfColumns = len(value)
            else:
                if matrixNumberOfColumns != len(value):
                    raise Exception
            r.append(value)
    matrixNumberOfRows = len(r)
    return (r,matrixNumberOfRows,matrixNumberOfColumns)

#### only used in part I

def yieldRowsInAllDirections(matrix,matrixNumberOfRows,matrixNumberOfColumns):
    # horizontal direction: -
    for row in matrix:
        yield row
    
    # vertical direction: |
    for c in range(matrixNumberOfColumns):
        resultingRow = []
        for r in range(matrixNumberOfRows):
            resultingRow.append(matrix[r][c])
        yield ''.join(resultingRow)

    # diagonal direction: /
    for line in giveAllLines(matrix, yieldLeftAndLowerPoints, advanceInDiagonalDirectionPositiveSlope):
        yield line

    # diagonal direction: \
    for line in giveAllLines(matrix, yieldRightAndLowerPoints, advanceInDiagonalDirectionNegativeSlope):
        yield line


def giveAllLines(matrix, startingPointYielder, advancer):
    for (s,t) in startingPointYielder():
        line = [matrix[s][t]]
        (S,T) = (s,t)
        # repeatedly advance from starting point until the end
        while(True):
            (i,j) = advancer(S,T)
            if (i,j) == (None,None):
                break
            line.append(matrix[i][j])
            (S,T) = (i,j)
        yield ''.join(line)

def yieldRightAndLowerPoints():
    for i in range(matrixNumberOfRows):
        yield (i,matrixNumberOfColumns-1)
    for j in range(matrixNumberOfColumns-1): # -1 to prevent counting (matrixNumberOfRows-1, matrixNumberOfColumns - 1) twice
        yield (matrixNumberOfRows-1,j)

def yieldLeftAndLowerPoints():
    for i in range(matrixNumberOfRows):
        yield (i,0)
    for j in range(1,matrixNumberOfColumns): # start at 1 to prevent counting (matrixNumberOfRows-1, 0) twice
        yield (matrixNumberOfRows-1,j)        
    
def advanceInDiagonalDirectionPositiveSlope(i,j):
    return advance(i,j, lambda a,b: (a-1,b+1))

def advanceInDiagonalDirectionNegativeSlope(i,j):
    return advance(i,j, lambda a,b: (a-1,b-1))

def advance(i,j, advancingFunction):
    I,J = advancingFunction(i,j)
    if isCoordinateValid(I,J):
        return (I,J)
    return (None,None)

def countRowMatches(row:list):
    return len(re.findall('XMAS',row))

def isCoordinateValid(i,j):
    return i in range(matrixNumberOfColumns) and j in range(matrixNumberOfRows)
#### only used in part I

#### only used in part II

def walkMatrix(matrix,matrixNumberOfRows,matrixNumberOfColumns):
    for i in range(matrixNumberOfRows):
        for j in range(matrixNumberOfColumns):
            yield processCell(matrix,i,j)
         
def processCell(matrix,i,j):
    middle = matrix[i][j]
    if middle != 'A':
        return False
    (leftLeg,rightLeg) = giveBothCrossLegs(matrix, i, j)
    return isLegValid(leftLeg) and isLegValid(rightLeg)

def isLegValid(leg:str):
    return leg == 'MAS' or leg == 'SAM'

def giveBothCrossLegs(matrix,i,j):
    leftUp = (i-1,j-1)
    rightDown = (i+1,j+1)
    leftDown = (i+1,j-1)
    rightUp = (i-1,j+1)

    if isCoordinateValid(*leftUp) and isCoordinateValid(*rightDown) and isCoordinateValid(*leftDown) and isCoordinateValid(*rightUp):
        leftLeg = getCell(matrix,*leftUp) + getCell(matrix,i,j) + getCell(matrix,*rightDown)
        rightLeg = getCell(matrix,*rightUp) + getCell(matrix,i,j) + getCell(matrix,*leftDown)
        return (leftLeg,rightLeg)
    return (None,None)

def getCell(matrix,i,j):
    return matrix[i][j]

#### only used in part II

def solvePartI():
    result = 0
    for row in yieldRowsInAllDirections(r,matrixNumberOfRows,matrixNumberOfColumns):
        forwardMatchCount = countRowMatches(row)
        backwardMatchCount = countRowMatches(row[::-1])
        result = result + forwardMatchCount + backwardMatchCount
    return result

def solvePartII():
    # option A is re-use part I:
    # - scan all diagonal lines and search for 'MAS' or 'SAM', while saving the position of A (middle of cross)
    # - combine the results of both diagonal slope on common A-positions

    # option B is just to linearly walk the matrix, and for each A-occurence check if its cross is an X-MAS

    # I think option B is easier, so we'll try that first
    count = 0
    for result in walkMatrix(r,matrixNumberOfRows,matrixNumberOfColumns):
        if result:
            count = count + 1
    return count


(r,matrixNumberOfRows,matrixNumberOfColumns) = readData('04/input.txt')

resultI = solvePartI()
print(resultI)

resultII = solvePartII()
print(resultII)