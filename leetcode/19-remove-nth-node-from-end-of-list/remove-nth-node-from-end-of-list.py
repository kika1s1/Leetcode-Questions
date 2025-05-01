# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            dummy = ListNode(0, head)  
            first = dummy
            second = dummy
            count = 0
            while first:
                if count > n: 
                    second = second.next
                first = first.next
                count += 1

            second.next = second.next.next
            return dummy.next  