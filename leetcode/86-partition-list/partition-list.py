# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessthan = ListNode()
        greather_or_equal = ListNode()
        l_start = lessthan
        g_start = greather_or_equal
        
        while head:
            if head.val >= x:
                greather_or_equal.next = head
                greather_or_equal = greather_or_equal.next
            else:
                lessthan.next = head
                lessthan = lessthan.next
            head = head.next
        
        greather_or_equal.next = None
        lessthan.next = g_start.next
        return l_start.next
