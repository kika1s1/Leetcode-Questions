# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Base cases: empty list or single node list
        if not head or not head.next:
            return head
        
        # Determine the length of the linked list
        length = 1
        curr = head
        while curr.next:
            length += 1
            curr = curr.next
        
        # Calculate the effective rotation amount within the range of the list size
        k = k % length
        
        # No rotation needed
        if k == 0:
            return head
        
        # Find the new head and tail nodes after rotation
        steps = length - k
        curr = head
        for _ in range(steps - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        
        # Connect the tail of the original list to the head
        curr = new_head
        while curr.next:
            curr = curr.next
        curr.next = head
        
        return new_head