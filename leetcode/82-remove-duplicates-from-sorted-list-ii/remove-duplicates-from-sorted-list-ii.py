# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode('d')
        prev = dummy
        current = head
        prev.next = current
        
        while current:
            while current.next and current.val == current.next.val:
                current = current.next

            if prev.next == current:
               prev = prev.next
            else:
                prev.next = current.next

            current = current.next
        return dummy.next