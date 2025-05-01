# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        level_value = {}
        queue = deque()
        queue.append(root)
        level = 1
        while len(queue) > 0:
            ql = len(queue)
            total = 0
            for i in range(ql):
                node = queue.popleft()
                if node:
                    total +=node.val
                    # level_val.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            level_value[level] = total
            level += 1
        maxim =  level_value[1]
        level = 1
        for i, j in level_value.items():
            if maxim < j:
                maxim = j
                level = i

        return level

        