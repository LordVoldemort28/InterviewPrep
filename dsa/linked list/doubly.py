class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    
    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        
        #If head doesn't exit
        if not self.head:
            self.insert(node)
            return
        
        #Check if head already node
        if self.head.value == node.value:
            return
        
        #Check if tail value wants to become head
        if self.tail.value == node.value:
            self.tail, self.head = self.head, self.tail
            return
        
        #Check if value already exists
        if self.containsNodeWithValue(node.value):
            node = self.getNodeWithValue(node.value)

            #Takeout node from its place and re-wire connection of next and prev node
            temp = self.head
            node.prev.next = node.next
            node.next.prev = node.prev
            
            #Connect node next to previous head and set node prev to tail
            node.next = temp
            node.prev = temp.prev
            
            #Connect previous head prev to node
            temp.prev = node
            
            #Set tail next to node
            node.prev.next = node
            
            #Set head to new node
            self.head = node
            return
        
        #Else node doesn't exist
        self.insert(node)
        self.tail, self.head = self.head, self.tail
    
    """
    Inserting element in last of linked list
    T -> O(1) and S -> O(1)
    """
    def insert(self, node):
        #If head and tail both are none
        if not self.head:
            self.head = node
            self.tail = self.head
        #If there's only one node which is head and tail both
        elif self.head == self.tail:
            #Make another node and assign tail
            self.tail = node
            
            #Make connection of head to tail
            self.head.next = self.tail
            self.head.prev = self.tail
            
            #Make connection of tail to head
            self.tail.next = self.head
            self.tail.prev = self.head
        #If both tail and head exist
        else:
            #Store next node from head
            temp = self.tail.next
            
            #Reroute next connections
            self.tail.next = node
            node.next = temp
            
            #Reroute previous connections
            temp.prev = node
            node.prev = self.tail
            
            self.tail = node

    def setTail(self, node):
        
        #if tail doesn't exist
        if not self.tail:
            self.insert(node)
        
        if self.tail.value == node.value:
            return
        
        #Check if tail value wants to become head
        if self.head.value == node.value:
            self.tail, self.head = self.head, self.tail
            return

        #Check if node value already exist
        if self.containsNodeWithValue(node.value):
            node = self.getNodeWithValue(node.value)
            
            #Takeout node from its place and re-wire connection of next and prev node
            temp = self.tail
            node.prev.next = node.next
            node.next.prev = node.prev
            
            #Set node next to heap and node prev to previous tail
            node.next = temp.next
            node.prev = temp
            
            #Set head prev to node
            temp.next.prev = node
            
            #Set previous tail next to node
            temp.next = node
            return
        
        self.insert(node)

    def insertBefore(self, node, nodeToInsert):
        
        if not self.containsNodeWithValue(node.value):
            return
        
        #Get existing node
        node = self.getNodeWithValue(node.value)
        
        if self.head is node:
            self.setHead(nodeToInsert)
        
        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        
        node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        
        if not self.containsNodeWithValue(node.value):
            return

        node = self.getNodeWithValue(node.value)
        
        if node == self.tail:
            pass
        
    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        pass

    def remove(self, node):
        # Write your code here.
        pass
    
    def getNodeWithValue(self, value):
        current = self.head
        visited = []
        
        while True:
            
            if current.value == value:
                return current
            
            if current in visited:
                break
            
            visited.append(current)
            current = current.next

    def containsNodeWithValue(self, value):
        
        current = self.head
        visited = []
        
        while True:
            
            if current.value == value:
                return True
            
            if current in visited:
                break
            
            visited.append(current)
            current = current.next
        
        return False
    
    def printBackwardLinkedList(self):

        visited = []
        current = self.tail

        while True:

            if current in visited:
                break

            visited.append(current)
            current = current.prev
            
        print(' <-> '.join([str(node) for node in visited]))
            
    def printForwardLinkedList(self):
        
        visited = []
        current = self.head
        
        while True:
            
            if current in visited:
                break
            
            visited.append(current)
            current = current.next
        
        print(' <-> '.join([str(node) for node in visited]))

def main():
    
    initArray = [1, 2, 3, 4, 5]
    
    dLinkedList = DoublyLinkedList()
    
    #Setup initial doubly linked list
    for el in initArray:
        dLinkedList.insert(Node(el))
    
    print("Set head to 6")
    dLinkedList.setHead(Node(4))
    dLinkedList.printForwardLinkedList()
    
    print("\nSet tail to 6")
    dLinkedList.setTail(Node(6))
    dLinkedList.printForwardLinkedList()
    dLinkedList.printBackwardLinkedList()
    
    print("\nInsert 3 before 6")
    dLinkedList.insertBefore(Node(6), Node(3))
    dLinkedList.printForwardLinkedList()
    
if __name__ == '__main__':
    main()
