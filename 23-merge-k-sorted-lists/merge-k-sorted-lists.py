# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for num in lists:
            while num:
                nums.append(num.val)
                num =  num.next
        nums.sort()
        dummyNode = ListNode()
        temp = dummyNode
        for num in nums:
            node = ListNode(num)
            temp.next = node
            temp = node
        return dummyNode.next