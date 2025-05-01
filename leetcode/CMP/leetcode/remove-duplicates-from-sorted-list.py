# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
            lst = []
            while head:
                lst.append(head.val)
                head = head.next
            lst = sorted(list(set(lst)))
            a = ListNode()
            temp = a
            for i in lst:
                temp.next = ListNode(i)
                temp = temp.next
            return a.next