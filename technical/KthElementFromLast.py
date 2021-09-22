class LinkedListNode(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
#Brute Force
def kth_to_last_node(k, head):

    # Return the kth to last node in the linked list
    length = 0

    current = head
    while current:

        length += 1
        current = current.next

    current = head

    for _ in range(length-k):
        current = current.next

    return current


fourth = LinkedListNode(4)
third = LinkedListNode(3, fourth)
second = LinkedListNode(2, third)
first = LinkedListNode(1, second)

print(kth_to_last_node(2, first).value)
