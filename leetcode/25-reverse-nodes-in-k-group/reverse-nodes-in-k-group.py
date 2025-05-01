# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        total_node = 0
        current = head
        while current:
            total_node +=1
            current = current.next
        dummy = ListNode()
        dummy.next = head
        previous_group_end  = dummy
        while total_node >=k:
            current = previous_group_end.next
            next_node = current.next  
            for _ in range(k - 1):
                current.next = next_node.next
                next_node.next = previous_group_end.next
                previous_group_end.next = next_node
                next_node = current.next
            previous_group_end = current  
            total_node -= k  
        return dummy.next

