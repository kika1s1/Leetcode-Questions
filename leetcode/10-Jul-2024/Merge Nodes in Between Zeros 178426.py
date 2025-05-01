# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tot = 0
        prev = head
        temp = prev
        head = head.next
        while head:
            if head.val ==0:
                prev.val =  tot
                if not head.next:
                    prev.next = None
                else:
                    prev = prev.next
                tot = 0
            else:
                tot +=head.val
            head = head.next
        
        return temp