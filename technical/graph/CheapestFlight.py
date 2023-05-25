from heapq import heappop, heappush
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        using bellman ford
        T -> (E * k)
        """
        
        dist = [float('inf')] * n
        dist[src] = 0
        
        for _ in range(k+1):
            tempDist = dist.copy()
            
            for a, b, w in flights:
                
                if dist[a] != float('inf') and dist[a] + w < tempDist[b]:
                    tempDist[b] = dist[a] + w
            
            dist = tempDist

        return -1 if dist[dst] == float('inf') else dist[dst]
    
    def findCheapestPriceDjikstra(self, n, flights, src, dst, k):

        #Djiktra with counting k moves
        graph = defaultdict(list)
        visited = defaultdict(lambda: float('inf'))

        for u, v, w in flights:
            graph[u].append((v, w))
        
        queue = [(0, -1, src)]
        
        while queue:
            
            cost, stops, node = heappop(queue)
            
            #have seen the node before and the stops are more than last time
            if visited[node] <= stops:
                continue
            
            if stops > k:
                continue
            
            if node == dst:
                return cost
            
            for neighbor, fare in graph[node]:
                
                newCost = cost+fare
                if stops + 1 < visited[neighbor]:
                    heappush(queue, (newCost, (stops+1), neighbor))
                    
        return -1



test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'n': 4,
            'flights': [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            'src': 0,
            'dst': 3,
            'k': 1
        },
        'output': 700,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': {
            'n': 13,
            'flights': [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]],
            'src': 10,
            'dst': 1,
            'k': 10
        },
        'output': 700,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().findCheapestPriceDjikstra(
        input['n'], input['flights'], input['src'], input['dst'], input['k'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
