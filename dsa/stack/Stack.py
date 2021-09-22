"""
Works on LIFO(Last in first out) principle

It follows the characteristics of linked list because removing 
and inserting from beinging of the list is O(1) or constant time

Time complexity:
    push    : O(1)
    pop     : O(1)
    peek    : O(1)
    size    : O(1)

Use case: 
    1. The call stack
    2. DFS
    3. String parsing
    4. Undo/Redo
    
Written by: Rahul Prajapati
"""

class SimpleStack():
    
    def __init__(self):
        self.stack = []
        
    def pop(self):
        if not self.stack:
            return None
            
        return self.stack.pop()
    
    def push(self, item):
        self.stack.append(item)
    
    def isEmpty(self):
        if not self.stack:
            return True
        
        return False
    
    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

class Node():
    
    def __init__(self, value):
        self.value = value
        self.next = None
        

def main():
    s = SimpleStack()
    print("Is stack empty = {}".format(s.isEmpty()))
    
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    
    print("Pop: {}".format(s.pop()))
    print("Pop: {}".format(s.pop()))
    print("Pop: {}".format(s.pop()))
    
    print("Peek: {}".format(s.peek()))
    return

if __name__ == '__main__':
    main()
