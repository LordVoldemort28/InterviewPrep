from operator import ne
import __init__
from collections import defaultdict
from dsa.disjointSet.Disjointset import DisjointSet

"""
Simple dfs approach
"""
class Forest:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdges(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

def getLargestTreeInForestBruteForce(edges):
    
    forest = Forest()
    
    for edge in edges:
        forest.addEdges(edge[0], edge[1])
    
    unknownPlants = [plant for plant in forest.graph.keys()]
    maxForest = float('-inf')
    
    #Checking each unknown plants
    while unknownPlants:
        
        currentPlant = unknownPlants.pop(0)
        
        #Search plants around current plant
        currentForest = [currentPlant]
        #Maintaining to not form cycle
        knownPlants = []
        currentCount = 1
        
        #Exploring forest around previous unknown plant
        while currentForest:
            
            current = currentForest.pop()
            knownPlants.append(current)
            for neighbor in forest.graph[current]:
                
                if neighbor not in knownPlants:
                    currentForest.append(neighbor)
                    unknownPlants.remove(neighbor)
                    currentCount += 1
                    
        maxForest = max(currentCount, maxForest)
        
    return maxForest

"""
Disjoint solution
"""
def getLargestTreeInForest(edges):
    djs = DisjointSet()

    for edge in edges:
        djs.union(edge[0], edge[1])

    count = defaultdict(int)
    for parent in djs.parent.keys():
        count[djs.find(parent)] += 1

    return max(count.values())
    

test_cases = {
    'test_case_1': {
        'description': 'two tree',
        'input': [(0, 1), (2, 3), (3, 4)],
        'output': 3,
        'active': True
    },
    'test_case_2': {
        'description': 'three tree',
        'input': [(0, 11), (4, 6), (4, 5), (5, 7), (8, 9), (9, 10)],
        'output': 4,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = getLargestTreeInForest(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
