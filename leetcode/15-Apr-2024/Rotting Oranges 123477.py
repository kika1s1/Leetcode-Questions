# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        current_node =root
        queue.append(current_node)
        ans = []

        while len(queue) > 0:
            
            level = []
            for i in range(len(queue)):
                current_node = queue.popleft()
                level.append(current_node.val)
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
            if level:
                ans.append(sum(level)/len(level))
        return ans
