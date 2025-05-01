# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls = []
        temp = head
        while temp:
            ls.append(temp.val)
            temp = temp.next
        return ls ==ls[::-1]
        