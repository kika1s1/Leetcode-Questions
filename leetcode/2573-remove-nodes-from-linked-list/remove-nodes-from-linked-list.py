# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        nodes = []

        while head:
            nodes.append(head.val)
            head = head.next
        for i in nodes:
            while stack and stack[-1] < i:
                stack.pop()
            stack.append(i)
        print(stack)
        if not stack:
            return None
        head = ListNode(stack[0])
        temp = head
        for i in range(1, len(stack)):
            new_node = ListNode(stack[i])
            temp.next = new_node
            temp = new_node


        return head