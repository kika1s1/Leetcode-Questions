"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = deque()
        if not root:
            return 0
        
        queue = [(root, 1)]
        max_depth = 0
        
        while queue:
            node, depth = queue.pop(0)
            max_depth = max(max_depth, depth)
            for child in node.children:
                queue.append((child, depth + 1))
        
        return max_depth

        