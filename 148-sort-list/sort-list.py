# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        nodes.sort()
        head = ListNode(0)
        temp = head
        for node in nodes:
            new_node = ListNode(node)
            temp.next = new_node
            temp = new_node
        return head.next
        