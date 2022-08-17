import heapq

"""
Written by: Rahul Prajapati

Time complexity: O(log N)

Use: Picking maximum item in list
Bonus: https://docs.python.org/3/library/heapq.html
"""

class MaxHeap(object):

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def push(self, item):
        heapq.heappush(self.heap, (-item))

    def pop(self):
        if not len(self):
            return None

        return -heapq.heappop(self.heap)

    def peek(self):
        if self.heap:
            return -self.heap[0]

    def __len__(self):
        return len(self.heap)

if __name__ == '__main__':
        
    maxHeap = MaxHeap()

    maxHeap.push(2)
    maxHeap.push(6)
    maxHeap.push(1)

    print(maxHeap.heap)  # [-6, -2, -1]

    print(maxHeap.pop()) # 6
    print(maxHeap.pop()) # 2
    print(maxHeap.pop()) # 1

    print(maxHeap.pop())
