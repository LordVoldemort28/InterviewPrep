class LinkedListNode(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def contains_cycle(first_node):

    # Check if the linked list contains a cycle

    visited = []

    while first_node.next:

        if first_node.value in visited:
            return True
        else:
            visited.append(first_node.value)
            first_node = first_node.next

    return False


fifth = LinkedListNode(5)
fourth = LinkedListNode(4, fifth)
third = LinkedListNode(3, fourth)
second = LinkedListNode(2, third)
first = LinkedListNode(1, second)
fifth.next = third
result = contains_cycle(first)

print(result)
