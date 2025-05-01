# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            two = []
            if node:
                if node:
                    ans.append(node.val)
                if node.left:
                    two.append(node.left)
                if node.right:
                    two.append(node.right)
                for node in reversed(two):
                    queue.appendleft(node)
        return ans
