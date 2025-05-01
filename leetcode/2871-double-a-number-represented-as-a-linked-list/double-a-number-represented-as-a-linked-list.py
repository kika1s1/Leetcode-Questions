# Definition for singly-linked list.
import sys

 # Increase the limit to accommodate the larger value
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = ""
        
        while head:
            s +=str(head.val)
            head = head.next
        dNode = ListNode(0)
        temp = dNode
        s = str(int(s) * 2)
        sys.set_int_max_str_digits(50000) 
        
        for i in range(len(s)):
            new_node = ListNode(int(s[i]))
            temp.next = new_node
            temp = new_node
        return dNode.next
            
            
        