# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Check if either list is empty, return the other list
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Determine the head of the merged list
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        # Current pointer to build the merged list
        current = head
        
        # Merge the lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append any remaining nodes from list1 or list2
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return head