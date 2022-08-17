import math

class MaxHeap:
    
    def __init__(self, array):
        self.heap = self.heapify(array)
    
    """
    Insert all items in array
    T -> O(NlogN) and S -> O(N)
    """
    def heapify(self, array):
        
        #Initialize array
        self.heap = []
        
        #Insert all elements
        for el in array:
            self.insert(el)
        
        return self.heap
    
    """
    Insert item in a heap
    T -> O(logN) and S -> O(1)
    """
    def insert(self, item):
        
        #First insert item to last of array
        self.heap.append(item)
        
        #Start re-balancing
        currentIdx = len(self.heap)-1
        parentIdx = self.getParent(currentIdx)
        
        #Check if parent is bigger then current then replace position
        while currentIdx > 0 and self.heap[currentIdx] > self.heap[parentIdx]:
            
            #Swap with parent
            self.heap[currentIdx], self.heap[parentIdx] = self.heap[parentIdx], self.heap[currentIdx]
            
            #Reset Index
            currentIdx = parentIdx
            parentIdx = self.getParent(currentIdx)

    """
    Delete root node from heap
    T -> O(logN) and S -> O(1)
    """
    def pop(self):
        
        root = self.heap[0]
        
        if len(self.heap) < 2:
            self.heap.pop()
            return root
        
        #Swap first element to last element and then pop
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        
        #Compare with left and right children until children are smaller
        #than last index
        currentIdx = 0
        leftIdx = self.getLeftChild(currentIdx)
        rightIdx = self.getRightChild(currentIdx)
        
        #Check if either child is alive
        while self.isValid(leftIdx) or self.isValid(rightIdx):
            
            #If both child are there
            if self.isValid(leftIdx) and self.isValid(rightIdx):
                
                #If both child are smaller than current
                if self.heap[currentIdx] >= self.heap[leftIdx] and self.heap[currentIdx] >= self.heap[rightIdx] :
                    break
                
                #Pick bigger value from both child and replace with current
                biggerIdx = rightIdx if self.heap[rightIdx] > self.heap[leftIdx] else leftIdx
                self.heap[biggerIdx], self.heap[currentIdx] = self.heap[currentIdx], self.heap[biggerIdx]
                currentIdx = biggerIdx
                
            #If only left child is alive
            elif self.isValid(leftIdx) and not self.isValid(rightIdx):
                #If left child is smaller than current then no need to replace
                if self.heap[leftIdx] <= self.heap[currentIdx]:
                    break
                
                self.heap[leftIdx], self.heap[currentIdx] = self.heap[currentIdx], self.heap[leftIdx]
                currentIdx = leftIdx
                
            #If only right child is alive
            elif self.isValid(rightIdx) and not self.isValid(leftIdx):
                #If right child is smaller than current then no need to replace
                if self.heap[rightIdx] <= self.heap[currentIdx]:
                    break
                
                self.heap[rightIdx], self.heap[currentIdx] = self.heap[currentIdx], self.heap[rightIdx]
                currentIdx = rightIdx
            else:
                print("Error this case is not handled")
            
            leftIdx = self.getLeftChild(currentIdx)
            rightIdx = self.getRightChild(currentIdx)    
            
        return root
    
    def __len__(self):
        return len(self.heap)
    
    def isValid(self, idx):
        return idx in range(len(self.heap))
    
    def peek(self):
        return self.heap[0]

    def getParent(self, i):
        return math.floor(i/2)
    
    def getLeftChild(self, i):
        #Added one to adjust with zero indexed array
        return (2*i)+1
    
    def getRightChild(self, i):
        #Added one to adjust with zero indexed array
        return ((2*i)+1)+1
    
def main():
    
    heap = MaxHeap([10, 20, 2, 15, 30, 2, 40, -2])
    print(heap.heap)

    for _ in range(len(heap)):
        print(heap.pop())
    pass

if __name__ ==  '__main__':
    main()
