# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        ans = [root.val]
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    level.append(node.left)
                    queue.append(node.left)
                if node.right:
                    level.append(node.right)
                    queue.append(node.right)
            if level:
                ans.append(level[-1].val)
        return ans

