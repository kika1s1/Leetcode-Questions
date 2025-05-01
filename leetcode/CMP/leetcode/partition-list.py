# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        great = []
        lessThan = []
        while head:
            if head.val >=x:
                great.append(head.val)
            else:
                lessThan.append(head.val)
            head = head.next
        print(lessThan)
        dum = ListNode(0)
        temp = dum
        for num in lessThan:
            node = ListNode(num)
            temp.next = node
            temp = node
        for num in great:
            node = ListNode(num)
            temp.next = node
            temp = node
        return dum.next
         

        