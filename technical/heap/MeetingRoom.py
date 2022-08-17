from heapq import heappush, heapreplace

class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort()
        heap = []
        
        for (start, end) in intervals:
            #Someone leaving the available room
            if heap and start >= heap[0]:
                heapreplace(heap, end)
            #Add room
            else:
                heappush(heap, end)
        return len(heap)
    
    def minMeetingRoomsSort(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start = []
        end = []
        
        for (iStart, iEnd) in intervals:
            start.append(iStart)
            end.append(iEnd)
            
        start.sort()
        end.sort()
        
        s = e = 0
        
        #numRooms is max room available so far
        numRooms = available = 0
        
        while s < len(start):
            #If new person comes in 
            if start[s] < end[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1
                s += 1
            #Someone left
            else:
                available += 1
                e += 1
            
        return numRooms

test_cases = {
    'test_case_1': {
        'description': 'normal test',
        'input': [[0, 30], [5, 10], [15, 20]],
        'output': 2,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': [[7, 10], [2, 4]],
        'output': 1,
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
    result = tool.minMeetingRooms(input)
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
