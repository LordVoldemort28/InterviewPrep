# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
import __init__
from dsa.heap import MaxHeap, MinHeap

class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.maxHeap = MaxHeap.MaxHeap()
        self.minHeap = MinHeap.MinHeap()

    def insert(self, num):
        
        #If num is greater than top element of max heap insert value in min heap
        if not self.maxHeap.peek() or self.maxHeap.peek() >= num:
            self.maxHeap.push(num)
        else:
            self.minHeap.push(num)
        
        #Re-balance both side
        
        #If difference between max heap and min heap is greater than 2 move
        #top element max heap to min heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            self.minHeap.push(self.maxHeap.pop())
        
        #If min heap has more elements than max heap move top min heap element to max heap
        elif len(self.minHeap) > len(self.maxHeap):
            self.maxHeap.push(self.minHeap.pop())

    def getMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (self.maxHeap.peek()+self.minHeap.peek())/2.0
        else:
            return float(self.maxHeap.peek())


test_cases = {
    'test_case_1': {
        'description': 'odd test',
        'input': [5, 10, 12, 13, -2, 0, 6, 14, 3],
        'output': 6.0,
        'active': True
    },
    'test_case_2': {
        'description': 'even test',
        'input': [5, 10, 12, -2, 0, 6, 14, 3],
        'output': 5.5,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue
    
    continuousHandler = ContinuousMedianHandler()
    input = data['input']
    
    for num in input:
        continuousHandler.insert(num)
        
    result = continuousHandler.getMedian()
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
