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

"""
Sliding window approach
T -> Faster than above
"""
def removeKthNodeFromEnd(head, k):
    # Write your code here.

    #loop through k elements from head
    left = head
    right = head
    for _ in range(k-1):
        right = right.next

    while right.next:

        prev = left
        left = left.next
        right = right.next

    if left.next:
        left.value = left.next.value
        left.next = left.next.next
    else:
        prev.next = None



fourth = LinkedListNode(4)
third = LinkedListNode(3, fourth)
second = LinkedListNode(2, third)
first = LinkedListNode(1, second)

print(kth_to_last_node(2, first).value)

