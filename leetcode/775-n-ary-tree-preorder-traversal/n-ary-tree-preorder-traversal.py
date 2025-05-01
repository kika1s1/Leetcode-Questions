"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def pre(root):
            if not root:
                return 
            ans.append(root.val)
            for i in range(len(root.children)):
                pre(root.children[i])
        pre(root)
        return ans