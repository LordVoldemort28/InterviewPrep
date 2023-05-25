class Graph:
    
    def __init__(self, nCourse, edges):
        self.nCourse = nCourse
        self.graph = self.makeSet(edges)
        
    def makeSet(self, edges):
        graph = {}
        for i in range(self.nCourse):
            graph[i] = []
        
        for (u, v) in edges:
            graph[u].append(v)
            
        return graph
    
    def topologicalSort(self):
        
        inDegree = [0] * self.nCourse
        queue = []
        topOrder = []
        
        #Record inDegree
        for vertex in self.graph.keys():
            for neighbor in self.graph[vertex]:
                inDegree[neighbor] += 1
        
        #Insert vertex with zero dependency
        for idx, degree in enumerate(inDegree):
            if degree == 0: 
                queue.append(idx)
        
        while queue:
            
            current = queue.pop(0)
            topOrder.append(current)
            
            for neighbor in self.graph[current]:
                
                inDegree[neighbor] -= 1
                
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        for degree in inDegree:
            if degree > 0:
                return []
            
        return topOrder[::-1]

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        return Graph(numCourses, prerequisites).topologicalSort()

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'numCourses': 4,
            'prerequisites': [[1, 0], [2, 0], [3, 1], [3, 2]]
        },
        'output': [0, 2, 1, 3],
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': {
            'numCourses': 2,
            'prerequisites': [[1, 0]]
        },
        'output': [0, 1],
        'active': True
    },
    'test_case_3': {
        'description': 'not possible test',
        'input': {
            'numCourses': 3,
            'prerequisites': [[1, 0], [0, 1]]
        },
        'output': [],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().findOrder(input['numCourses'], input['prerequisites'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
