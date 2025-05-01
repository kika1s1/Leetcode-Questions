# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        cnt = 0
        checked = False
        while head:
            if head.val not in nums and checked:
                cnt +=1
                checked = False
            if head.val in nums:
                checked =  True
            head = head.next
        return cnt+1 if checked else cnt
