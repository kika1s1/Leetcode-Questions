# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reversed_node = []
        def recursion(head):
            if not head:
                return 
            recursion(head.next)
            reversed_node.append(head)
        recursion(head)
        cnt = 0
        while head:
            if head.val != reversed_node[cnt].val:
                return False
            head = head.next
            cnt +=1
        return True

        