from heapq import heapify, heappop, heappush


"""
Written by: Rahul Prajapati

Time complexity: O(log N)

Use: Picking item based on priority in the queue list
Bonus: https://docs.python.org/3/library/heapq.html
"""

class PriorityQueue:

    def __init__(self):
        self.heap = []
        heapify(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)


class QueueNode:

    def __init__(self, val, priority):
        self.val = val
        self.priority = priority

    def __lt__(self, node):
        return self.priority < node.priority

heap = PriorityQueue()

heap.push(QueueNode('rahul', 3))
heap.push(QueueNode('shivani', 2))
heap.push(QueueNode('shiv', 1))
heap.push(QueueNode('achintya', 2))

print(heap.pop().val) #shiv
print(heap.pop().val) #shivani
print(heap.pop().val) #achintya
print(heap.pop().val) #rahul
