class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        ref = {}

        cHead = cCurrent = Node(head.val)
        current = head
        ref[current] = cCurrent

        while current.next:

            current = current.next
            temp = Node(current.val)
            cCurrent.next = temp

            ref[current] = temp
            cCurrent = cCurrent.next

        ref[None] = cCurrent.next

        cCurrent = cHead
        current = head

        while current:

            cCurrent.random = ref[current.random]

            cCurrent = cCurrent.next
            current = current.next

        return cHead
