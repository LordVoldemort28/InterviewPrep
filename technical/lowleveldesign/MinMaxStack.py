import __init__
from dsa.stack.Stack import SimpleStack

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
        
class MinMaxStack():

    def __init__(self):
        self.stack = SimpleStack()
        self.max = SimpleStack()
        self.min = SimpleStack()

    def push(self, item):
        self.stack.push(item)

        if self.getMin() == None or self.getMin() >= item:
            self.min.push(item)

        if self.getMax() == None or self.getMax() <= item:
            self.max.push(item)

    def getMin(self):
        return self.min.peek()

    def getMax(self):
        return self.max.peek()

    def peek(self):
        return self.stack.peek()

    def pop(self):

        item = self.stack.pop()

        if self.getMax() == item:
            self.max.pop()

        if self.getMin() == item:
            self.min.pop()

        return item

def main():
    mmStack = MinMaxStack()
    
    mmStack.push(5)
    mmStack.push(5)
    mmStack.push(5)
    mmStack.push(5)
    mmStack.push(8)
    mmStack.push(8)
    mmStack.push(0)
    mmStack.push(8)
    mmStack.push(9)
    mmStack.push(5)
    mmStack.pop() #5
    mmStack.pop() #9
    mmStack.pop() #8
    print(mmStack.getMin())
    print(mmStack.getMax())
    print(mmStack.peek())
if __name__ == '__main__':
    main()
