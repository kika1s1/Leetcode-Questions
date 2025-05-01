# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        before = None
        while head:
            after = head.next
            head.next = before
            before = head
            head = after

        return before