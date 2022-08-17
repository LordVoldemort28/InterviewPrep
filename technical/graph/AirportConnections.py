from operator import ne


class Graph:
    
    def __init__(self, airports, connections):
        self.graph = self.makeGraph(airports, connections)
        
    def makeGraph(self, airports, connections):
        
        graph = {}
        
        for idx in range(len(airports)):
            graph[idx] = []
            
        for (src, dest) in connections:
            
            srcIdx = airports.index(src)
            destIdx = airports.index(dest)
            
            graph[destIdx].append(srcIdx)
            
        return graph

def getMinimumVertex(dist, visited):
    
    minVertex = 0
    minDist = float('inf')
    
    for idx, distance in enumerate(dist):
        
        if distance < minDist and idx not in visited:
            minDist = distance
            minVertex = idx
            
    return minVertex

def airportConnections(airports, connections, startingAirport):

    graph = Graph(airports, connections)
    
    dist = [float("inf")] * len(airports)
    
    dist[airports.index(startingAirport)] = 0
    visited = []
    
    while len(visited) < len(airports):
        
        current = getMinimumVertex(dist, visited)
        visited.append(current)
        
        for neighbor in graph.graph[current]:
            
            if neighbor not in visited and dist[current] + 1 < dist[neighbor]:
                dist[neighbor] = dist[current] + 1
                
    print(dist)
    pass


test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'airports': ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"],
            'connections': [
                ["DSM", "ORD"],
                ["ORD", "BGI"],
                ["BGI", "LGA"],
                ["SIN", "CDG"],
                ["CDG", "SIN"],
                ["CDG", "BUD"],
                ["DEL", "DOH"],
                ["DEL", "CDG"],
                ["TLV", "DEL"],
                ["EWR", "HND"],
                ["HND", "ICN"],
                ["HND", "JFK"],
                ["ICN", "JFK"],
                ["JFK", "LGA"],
                ["EYW", "LHR"],
                ["LHR", "SFO"],
                ["SFO", "SAN"],
                ["SFO", "DSM"],
                ["SAN", "EYW"]
            ],
            'startingAirports': 'LGA'
        },
        'output': 3,
        'active': False
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': {
            'airports': ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"],
            'connections': [
                ["LGA", "DSM"],
                ["DSM", "ORD"],
                ["SIN", "BGI"],
                ["SIN", "CDG"],
                ["CDG", "DEL"],
                ["DEL", "DOH"],
                ["DEL", "CDG"],
                ["DEL", "EWR"],
                ["HND", "ICN"],
                ["ICN", "JFK"],
                ["JFK", "LGA"],
                ["JFK", "SFO"],
                ["EYW", "LHR"],
                ["SFO", "ORD"],
                ["SFO", "LGA"],
                ["SFO", "SIN"],
                ["CDG", "EYW"],
                ["ORD", "HND"],
                ["HND", "SAN"],
                ["LGA", "TLV"],
                ["LGA", "BUD"]
            ],
            'startingAirports': 'LGA'
        },
        'output': 0,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = airportConnections(
        input['airports'], input['connections'], input['startingAirports'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
