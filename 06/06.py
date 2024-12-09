directions = ['N','E','S','W']
valueStartingPoint = '^'
valueObstacle = '#'
valueClear = '.'
valueOffGrid = 'OFFGRID'
valueVisited = 'X'

def readData(filename):
    r = []
    rowNumber = 0
    startX = None
    startY = None

    with open(filename, 'r') as file:
        for line in file:
            value = line.replace('\n','')
            if rowNumber == 0:
                matrixNumberOfColumns = len(value)
            else:
                if matrixNumberOfColumns != len(value):
                    raise Exception
            for col in range(matrixNumberOfColumns):
                if value[col] == valueStartingPoint:
                    if (startX,startY) != (None,None): # make sure there is at most 1 starting point
                        raise Exception
                    startX = rowNumber
                    startY = col
            r.append(value)
            rowNumber = rowNumber + 1
    matrixNumberOfRows = len(r)
    if (startX,startY) == (None,None): # make sure there is at least 1 starting point
        raise Exception
    return (r,matrixNumberOfRows,matrixNumberOfColumns,startX,startY)

# for debugging (and illustration) purposes, prettify the updated grid
def pretty(r):
    s = ''
    for row in range(matrixNumberOfRows):
        s = s + '\n'
        for col in range(matrixNumberOfColumns):
            s = s + r[row][col]
    return s

def advanceInDirection(x,y,direction):
    if direction == 'N':
        f = lambda a,b: (a-1,b)
    elif direction == 'E':
        f = lambda a,b: (a,b+1)
    elif direction == 'S':
        f = lambda a,b: (a+1,b)
    elif direction == 'W':
        f = lambda a,b: (a,b-1)
    (X,Y) = advance(x,y, f)
    if (X,Y) == (None,None):
        return (X,Y,valueOffGrid)
    return (X,Y,s[X][Y])

def advance(i,j, advancingFunction):
    I,J = advancingFunction(i,j)
    if isCoordinateValid(I,J):
        return (I,J)
    return (None,None)

def isCoordinateValid(i,j):
    return i in range(matrixNumberOfColumns) and j in range(matrixNumberOfRows)

def rotate(direction):
    i = directions.index(direction)
    nextI = (i+1) % len(directions)
    return directions[nextI]

def solvePartI():
    result = 1
    (x,y) = (startX,startY)
    s[x][y] = valueVisited
    direction = 'N'
    while(True):
        (X,Y, value) = advanceInDirection(x,y,direction)
        if value == valueOffGrid:
            return result
        elif value == valueObstacle:
            direction = rotate(direction)  
        else:
            if value != valueVisited:
                result = result + 1
            (x,y) = (X,Y)
            s[X][Y] = valueVisited
            #print(pretty(s))          

def copy(r):
    result = []
    for row in range(matrixNumberOfRows):
        resultRow = []
        for col in range(matrixNumberOfColumns):
            resultRow.append(r[row][col])
        result.append(resultRow)
    return result

(r,matrixNumberOfRows,matrixNumberOfColumns,startX,startY) = readData('06/input.txt')
s = copy(r)
resultI = solvePartI()
print(resultI)
print(pretty(s))