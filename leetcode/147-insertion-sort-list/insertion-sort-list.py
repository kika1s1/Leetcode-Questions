# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)  # Dummy node to handle the sorted list
        dummy.next = head
        sorted_tail = head  # Pointer to the tail of the sorted list
        
        current = head.next  # Pointer to the current node to be inserted
        
        while current:
            if current.val >= sorted_tail.val:
                sorted_tail = sorted_tail.next
            else:
                prev = dummy
                while prev.next.val < current.val:
                    prev = prev.next
                
                sorted_tail.next = current.next
                current.next = prev.next
                prev.next = current
                
            current = sorted_tail.next
        
        return dummy.next