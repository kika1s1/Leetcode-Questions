# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        queue = deque()
        while head:
            queue.append(head.val)
            head = head.next
        maxim = float("-inf")
        while queue:
            two_sum = queue.popleft() + queue.pop() 
            if two_sum > maxim:
                maxim = two_sum
        return maxim
        