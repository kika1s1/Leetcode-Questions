# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        a = l1.val + l2.val
        head = ListNode(a % 10)
        head.next = self.addTwoNumbers(l1.next, l2.next)
        if a >= 10:
            head.next = self.addTwoNumbers(head.next, ListNode(1))
        return head