# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        heap  = []
        for index, node in enumerate(lists):
            if node:
                heappush(heap, (node.val,index, node.next))
        while heap:
            value,index, node = heappop(heap)
            temp.next = ListNode(value)
            temp = temp.next
            if node:
                    heappush(heap, (node.val,index,  node.next))
        return dummy.next
