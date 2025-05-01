# Problem: Swapping Nodes in a Linked List - https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        for i in range(k):
            prev = head
            head = head.next
        f = prev
        slow = temp
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next
        f.val, slow.val = slow.val, f.val
        return temp
        