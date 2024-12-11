from itertools import product
import time
from typing import Any, Callable

addition = '+'
multiplication = '*'
concatenation = '|'


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
    result = []
    with open(filename, 'r') as file:
        for line in file:
            cleanLine = line.replace('\n','')
            splitted = cleanLine.split(':')

            x = int(splitted[0])
            y = list(map(int,splitted[1].split()))
            result.append((x,y))
    return result

def getPossibleOperatorSets(operatorAtoms,l):
    # yield all 2^l combinations of + and *
    return list(product(operatorAtoms, repeat=l))

def equationResult(abstractEquation,operatorAtoms):
    result, parts = abstractEquation

    possibleOperatorSets = getPossibleOperatorSets(operatorAtoms,len(parts)-1)
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
    elif operator == concatenation:
        return int(str(x)+str(y))
    else:
        raise Exception

def countBoolean(b: bool):
    if b:
        return 1
    return 0

def solvePartI(data):
    return sum(map(lambda e: equationResult(e,[addition, multiplication]), data))

def solvePartII(data):
    return sum(map(lambda e: equationResult(e,[addition, multiplication,concatenation]), data))

data = readData('07/test-input.txt')
executeAndTime(solvePartI,data)
executeAndTime(solvePartII,data)
