"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if not root:
            return result
        node_stack = [root]
        while node_stack:
            current_node = node_stack.pop()
            result.append(current_node.val)
            for child in current_node.children:
                node_stack.append(child)
        result.reverse()
        return result