class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2, carry=0, sum=None):

        if l1 or l2:

            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            total = num1 + num2 + carry
            
            carry, last_digit = divmod(total, 10)

            sum = self.insert(sum, last_digit)

            l1_next = l1.next if l1 else None
            l2_next = l2.next if l2 else None

            return self.addTwoNumbers(l1_next, l2_next, carry, sum)

        if carry != 0:
            sum = self.insert(sum, carry)

        return sum

    def insert(self, root, val):

        if root is None:
            return ListNode(val)

        current = root

        while current.next:
            current = current.next

        current.next = ListNode(val)

        return root

    def print(self, head):
        current = head
        
        number = []

        while current:

            number.append(str(current.val))
            current = current.next
        
        print(''.join(reversed(number)))


###############Test 1###############
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# tool = Solution()
# result = tool.addTwoNumbers(l1, l2)

# tool.print(result)

#
###############Test 2###############
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

tool = Solution()
result = tool.addTwoNumbers(l1, l2)

tool.print(result)
