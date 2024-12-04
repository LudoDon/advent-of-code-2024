import re
from functools import reduce

def readData(filename):
    r = ''
    with open(filename, 'r') as file:
        for line in file:
            r = r + line            
    return r

def stringToMatchingPairs(s:str):
    # mul(digit,digit) where both digits are captured
    pattern = 'mul\((\d+),(\d+)\)'
    # return list of pairs ('5','6') for each match mul(5,6)
    return re.findall(pattern, s)

def stringToMatchingPairsIncludingIndex(s:str):
    # mul(digit,digit) where both digits are captured
    pattern = 'mul\((\d+),(\d+)\)'
    # return list of matching objects
    # e.g. mul(5,6) has value ('5','6') and span (start,end) where start/end is the start/end index in the string
    return list(re.finditer(pattern, s))

def findEnablesWithIndex(s:str):
    pattern = 'do\(\)'    
    return list(re.finditer(pattern, s))

def findDisablesWithIndex(s:str):
    pattern = 'don\'t\(\)'    
    return list(re.finditer(pattern, s))

def processPair(pair):
    x,y = pair
    return int(x)*int(y)

dataString = readData('03/input.txt')

# answer to part a:
#pairs = stringToMatchingPairs(dataString)
#r = reduce(lambda a,b: a+b,map(processPair, pairs))

pairs = stringToMatchingPairsIncludingIndex(dataString)
enables = list(map(lambda x: x.start(), findEnablesWithIndex(dataString)))
disables =  list(map(lambda x: x.start(), findDisablesWithIndex(dataString)))

enabledPairs = []
for pair in pairs:
    index = pair.start()

    # we take the maximum of all smaller indexes -> this feels like O(n^2) and could easily be optimized:
    # e.g. keeping track of maximum so far and manually advancing both iterators until our current index is reached
    # but I don't feel like optimizing (premature)
    maxEnable = max([e for e in enables if e < index], default=0)
    maxDisable = max([d for d in disables if d < index], default=0)
    if maxDisable <= maxEnable:        
        enabledPairs.append((pair.group(1),pair.group(2)))
        

r = reduce(lambda a,b: a+b,map(processPair, enabledPairs))
print(r)