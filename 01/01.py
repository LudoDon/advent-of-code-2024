def readData(filename):
    x = []
    y = []
    with open(filename, 'r') as file:
        for line in file:
            splitted = line.split()
            xInt = int(splitted[0])
            yInt = int(splitted[1])
            x.append(xInt)
            y.append(yInt)
    return (x,y)

def processData(x:list,y:list):
    x.sort()
    y.sort()
    xi = iter(x)
    yi = iter(y)

    result = 0
    stop = False
    while(not stop):
        try:
            distance = next(xi) - next(yi)
            result = result + abs(distance)
        except StopIteration:
            stop = True
    return result


(x,y) = readData('2024-01-input.txt')
processData(x,y)
