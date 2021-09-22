import heapq

"""
Written by: Rahul Prajapati

Time complexity: O(log N)

Use: Picking minimum item in list
Bonus: https://docs.python.org/3/library/heapq.html
"""

class MinHeap(object):

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        if not len(self):
            return None

        return heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)


minHeap = MinHeap()

minHeap.push(2)
minHeap.push(6)
minHeap.push(1)

print(minHeap.pop())
print(minHeap.pop())
print(minHeap.pop())

print(len(minHeap))
