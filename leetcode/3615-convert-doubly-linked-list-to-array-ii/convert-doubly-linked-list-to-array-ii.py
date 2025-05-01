"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        left = []
        right = []
        temp = node
        while temp:
            right.append(temp.val)
            temp = temp.next
        while node:
            left.append(node.val)
            node = node.prev
        return left[::-1] + right[1:]