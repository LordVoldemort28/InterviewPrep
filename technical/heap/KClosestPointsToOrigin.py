from math import pow, sqrt
import __init__
from dsa.heap.MinHeap import MinHeap

class DistanceNode:
    def __init__(self, point, distance):
        self.point = point
        self.distance = distance
        
    def __lt__(self, node):
        return self.distance < node.distance
    
class Solution(object):
    
    def getDistance(self, x, y):
        return sqrt(pow(x, 2)+pow(y,2))

    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distances = MinHeap()
        
        for (x, y) in points:
            distances.push(DistanceNode([x, y], self.getDistance(x, y)))
        
        result = []
        for i in range(k):
            result.append(distances.pop().point)
            
        return result


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'points': [[3, 3], [5, -1], [-2, 4]],
            'k': 2
        },
        'output': [[3, 3], [-2, 4]],
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    tool = Solution()
    result = tool.kClosest(input['points'], input['k'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
