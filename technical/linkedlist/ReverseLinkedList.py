class LinkedListNode(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(head_of_list):

    # Reverse the linked list in place
    if head_of_list is None or head_of_list.next is None:
        return head_of_list

    prev = None
    current = head_of_list
    next_ = current.next

    while next_ is not None:

        current.next = prev
        prev = current
        current = next_
        next_ = current.next

    current.next = prev
    return current


sixth = LinkedListNode(6)
fifth = LinkedListNode(5, sixth)
fourth = LinkedListNode(4, fifth)
third = LinkedListNode(3, fourth)
second = LinkedListNode(2, third)
first = LinkedListNode(1, second)

print(reverse(first).value)
