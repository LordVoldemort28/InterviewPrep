from matplotlib.pyplot import get


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(size):
    
    if size == 0:
        return None
    
    head = LinkedList(1)
    current = head
    
    for i in range(2, size+1):
        current.next = LinkedList(i)
        current = current.next
        
    return head

test_cases = {
    'test even numbers': {
        'input': create_linked_list(6)
    },
    'test odd numbers': {
        'input': create_linked_list(7)
    },
    'test single node': {
        'input': create_linked_list(1)
    },
    'test no node': {
        'input': create_linked_list(0)
    }
}

def print_linked_list(head):
    
    current = head
    
    while current:
        print(current.value, end="->")
        current = current.next
    
    print("None")

def get_second_last(head):
    
    if not head.next:
        return head
    
    current = head
    
    while current.next.next:
        
        current = current.next
    
    return current

def zipped_linked_list(head):
    
    if not head:
        return head
    
    current = head
    
    while True:
        
        last = get_second_last(current)
        
        if current is last:
            break
        
        #Temporarily store next node from current
        temp = current.next
        
        #Redirect current next pointer to last node
        current.next = last.next
        
        #Make second last node next to None
        last.next = None
        
        #Reference back temporarily stored node to new current next node
        current.next.next = temp
        
        #Move current pointer to two place from current
        current = current.next.next
        
    return head


for test_key in test_cases:
    
    test = test_cases[test_key]
    input = test['input']
    
    print("============ {} ================".format(test_key))
    print("Input: ", end="")
    print_linked_list(input)
    print("Output: ", end="")
    print_linked_list(zipped_linked_list(input))
    print("===================================\n")

