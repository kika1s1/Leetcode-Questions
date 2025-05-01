# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head):
        dummyNode = ListNode(0)
        dummyNode.next = head
        mp = {}
        mp[0] = dummyNode
        prefSum = 0

        while head:
            prefSum += head.val
            if prefSum in mp:
                start = mp[prefSum] 
                pf = prefSum
                temp = start
                while temp.next != head:
                    temp = temp.next
                    pf += temp.val
                    del mp[pf]
                start.next = head.next
            else:
                mp[prefSum] = head
            head = head.next

        newHead = dummyNode.next
        del dummyNode
        return newHead