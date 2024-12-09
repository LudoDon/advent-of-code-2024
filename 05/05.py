from functools import cmp_to_key

def addToGraph(graph,x,y):
    if x not in graph:
        graph[x] = {y}        
    elif y not in graph[x]:
        graph[x].add(y)

def readData(filename):
    graph = {}
    updates = []
    with open(filename, 'r') as file:
        for line in file:
            value = line.replace('\n','')
            if '|' in value:
                values = list(map(int,value.split('|')))
                addToGraph(graph,values[0],values[1])
            if ',' in value:
                values = list(map(int,value.split(',')))
                if len(values) % 2 == 0:
                    raise Exception
                updates.append(values)            
    return (graph,updates)

(graph,updates) = readData('05/input.txt')
      
def comparable(x,y):
    return x in graph and y in graph[x]

def compare(x,y):
    if comparable(x,y):
        return -1
    if not comparable(y,x):
        raise Exception
    return -compare(y,x)

def customSort(l:list):  
    return list(sorted(l, key=cmp_to_key(compare)))

def listIsOk(l:list):  
    return l == customSort(l)

def process(l:list):  
    if not listIsOk(l):
        return 0
    return middleOf(l)

def middleOf(l:list): 
    half = len(l) // 2
    return l[half]

def solve(processor):
    result = 0
    for u in updates:
        result = result + processor(u)
    return result

def processII(l:list):  
    s = customSort(l)
    if (s == l):
        return 0
    return middleOf(s)

resultI = solve(process)
print(resultI)

resultII = solve(processII)
print(resultII)