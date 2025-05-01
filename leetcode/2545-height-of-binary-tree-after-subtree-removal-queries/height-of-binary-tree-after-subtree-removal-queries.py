from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height_map = {}  
        depth_map = {}   
        max_height_at_depth = {} 
        second_max_height_at_depth = {} 

        def dfs(node, depth):
            if not node:
                return 0
            depth_map[node.val] = depth
            left_height = dfs(node.left, depth + 1)
            right_height = dfs(node.right, depth + 1)
            current_height = max(left_height, right_height) + 1
            height_map[node.val] = current_height

            if depth not in max_height_at_depth or current_height > height_map[max_height_at_depth[depth]]:
                second_max_height_at_depth[depth] = max_height_at_depth.get(depth, 0)
                max_height_at_depth[depth] = node.val
            elif depth not in second_max_height_at_depth or current_height > height_map.get(second_max_height_at_depth[depth], 0):
                second_max_height_at_depth[depth] = node.val

            return current_height

        dfs(root, 0)

        result = []
        for node_val in queries:
            depth = depth_map[node_val]
            if max_height_at_depth[depth] == node_val:
                result.append(depth + height_map.get(second_max_height_at_depth[depth], 0) - 1)
            else:
                result.append(depth + height_map[max_height_at_depth[depth]] - 1)

        return result
