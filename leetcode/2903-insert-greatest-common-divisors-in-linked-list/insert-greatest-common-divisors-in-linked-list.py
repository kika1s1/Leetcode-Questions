# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            
            while b != 0:
                a, b = b, a % b
            return a
        
        if not head:

            return
        prev = head
        next_node = head.next
        while next_node:
            gc = gcd(next_node.val, prev.val)
            new_node = ListNode(gc)
            prev.next = new_node
            new_node.next = next_node
            prev = next_node
            next_node = next_node.next
        return head
            