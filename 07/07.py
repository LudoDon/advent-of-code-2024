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

def equationResult(abstractEquation,operatorAtoms):
    result, parts = abstractEquation

    if isEquationSatisfied(result, parts, operatorAtoms):
            return result
    return 0

def isEquationSatisfied(result, parts, operatorAtoms):
    if addition in operatorAtoms and multiplication in operatorAtoms:
        return isEquationSatisfiedAdditionMultiplication(result,parts, concatenation in operatorAtoms)
    
def isEquationSatisfiedAdditionMultiplication(result, parts, allowConcatenation):

    if len(parts) == 1:
        return result == parts[0]
    
    # start at end, recursively apply inverse operators
    diff = result - parts[-1]
    if diff == 0:
        return True
    if diff > 0 and isEquationSatisfiedAdditionMultiplication(diff, parts[:-1],allowConcatenation):
        return True
    
    if result % parts[-1] == 0:
        quotient = result // parts[-1]
        if quotient == 1:
            return True
        if isEquationSatisfiedAdditionMultiplication(quotient, parts[:-1], allowConcatenation):
            return True
            
    if allowConcatenation:
        lastPart = str(parts[-1])
        resultString = str(result)
        if resultString.endswith(lastPart):
            beginning = int(resultString[0:len(resultString)-len(lastPart)])
            if isEquationSatisfiedAdditionMultiplication(beginning, parts[:-1], allowConcatenation):
                return True

    return False

def countBoolean(b: bool):
    if b:
        return 1
    return 0

def solvePartI(data):
    return sum(map(lambda e: equationResult(e,[addition, multiplication]), data))

def solvePartII(data):
    return sum(map(lambda e: equationResult(e,[addition, multiplication,concatenation]), data))

data = readData('07/input.txt')
executeAndTime(solvePartI,data)
executeAndTime(solvePartII,data)
