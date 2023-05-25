# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def mergeTwoLists(self, l1, l2):

        if l1 and l2:
            if l1.val <= l2.val:
                self.insert(l1.val)
                return self.mergeTwoLists(l1.next, l2)
            else:
                self.insert(l2.val)
                return self.mergeTwoLists(l1, l2.next)
        elif l1 and not l2:
            self.insert(l1.val)
            return self.mergeTwoLists(l1.next, None)
        elif not l1 and l2:
            self.insert(l2.val)
            return self.mergeTwoLists(None, l2.next)
        else:
            return self.head

    def insert(self, num):

        if not self.head:
            self.head = ListNode(num)
            return
        elif self.head and not self.tail:
            self.tail = ListNode(num)
            self.head.next = self.tail
            return
        else:
            temp = ListNode(num)
            self.tail.next = temp
            self.tail = temp
