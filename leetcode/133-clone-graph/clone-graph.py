"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}
        
        stack = [node]
        old_to_new[node] = Node(node.val)  
        while stack:
            nod = stack.pop()
            for neighbor in nod.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                
                old_to_new[nod].neighbors.append(old_to_new[neighbor])
        
        return old_to_new[node]