class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert_tail(val, root=None):

    if root is None:
        return ListNode(val)

    current = root

    while current.next:
        current = current.next
    current.next = ListNode(val)

    return root


def ll_print(head):
    current = head

    while current:
        print(current.val)
        current = current.next


ll = insert_tail(1)

insert_tail(2, ll)
insert_tail(3, ll)

ll_print(ll)
