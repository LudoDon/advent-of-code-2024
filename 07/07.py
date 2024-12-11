from itertools import product

addition = '+'
multiplication = '*'

def readData(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            cleanLine = line.replace('\n','')
            splitted = cleanLine.split(':')

            x = int(splitted[0])
            y = list(map(int,splitted[1].split()))
            result.append((x,y))
    return result

def getPossibleOperatorSets(l):
    # yield all 2^l combinations of + and *
    return list(product([addition, multiplication], repeat=l))

def equationResult(abstractEquation):
    result, parts = abstractEquation

    possibleOperatorSets = getPossibleOperatorSets(len(parts)-1)
    for operators in possibleOperatorSets:
        if isEquationSatisfied(result, parts, operators):
            return result
    return 0

def isEquationSatisfied(result, parts, operators):
    return result == computeExpressionRecursive(parts,operators)

def computeExpressionRecursive( parts, operators):
    if len(parts) < 2:
        raise Exception
    r = computeBasicExpression(parts[0], operators[0], parts[1])
    if len(parts) > 2:
        return computeExpressionRecursive([r] + parts[2:], operators[1:])
    else:
        return r

def computeBasicExpression( x, operator, y):
    if operator == addition:
        return x + y
    elif operator == multiplication:
        return x * y
    else:
        raise Exception

def countBoolean(b: bool):
    if b:
        return 1
    return 0

def solvePartI(data):
    return sum(map(equationResult, data))

data = readData('07/input.txt')
(resultI) = solvePartI(data)
print(resultI)
