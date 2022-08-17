"""
Works on FIFO(First in first out) principle

A queue is linear abstract data type that can contain a long list of elements.
But important is how they can grow and shrink in size.

Time complexity:
    enqueue: O(1)
    dequeue: O(1)
    isEmpty: O(1)
    size   : O(1)

Use case: 
    1. BFS
    2. Printer
    3. Job Scheduling
    
Written by: Rahul Prajapati
"""

class SimpleQueue():
    
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.queue)
        
def main():
    q = SimpleQueue()
    
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    
    print("Dequeue: {}".format(q.dequeue()))
    print("Dequeue: {}".format(q.dequeue()))
    print("Dequeue: {}".format(q.dequeue()))
    
    print(q.queue)
    return

if __name__ == '__main__':
    main()
