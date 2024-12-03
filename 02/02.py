def readData(filename):
    r = []
    with open(filename, 'r') as file:
        for line in file:
            values = list(map(int,line.split()))
            r.append(values)
    return r

def isRowSafe(row:list):
    previous = None
    previousDiff = None
    for x in row:
        if previous is None:
            previous = x
            continue
        diff = x - previous

        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if previousDiff is not None and (diff < 0) != (previousDiff < 0): # sign flip
            return False

        previous = x
        previousDiff = diff
    return True

def isRowSafeV2(row:list):
    # naive brute force
    for i in range(len(row)):
        modifiedRow = []
        for j in range(len(row)):
            if i != j:
                modifiedRow.append(row[j])
        if isRowSafe(modifiedRow):
            return True                
    return False

    
def processRows(rows:list, validator):
    result = 0
    for row in rows:
        if validator(row):
            result = result + 1
    return result


# r = processRows(readData('02/input.txt'), isRowSafe)
r = processRows(readData('02/input.txt'), isRowSafeV2)
print(r)
