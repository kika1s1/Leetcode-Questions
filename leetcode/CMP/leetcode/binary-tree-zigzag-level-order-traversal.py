# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        results = []
        while queue:
            lq = len(queue)
            level = []
            for i in range(len(queue)):
                node = queue.popleft()

                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                results.append(level)
        for i in range(len(results)):
            if i%2 == 0:
                continue
            else:
                results[i].reverse()
        return results

        