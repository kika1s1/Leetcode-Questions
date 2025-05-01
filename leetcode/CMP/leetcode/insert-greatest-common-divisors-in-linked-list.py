# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while fast:
            v1 = slow.val
            v2 = fast.val
            gc = gcd(v1, v2)
            node = ListNode(gc)
            slow.next = node
            node.next = fast
            slow = fast
            fast= fast.next
        return head