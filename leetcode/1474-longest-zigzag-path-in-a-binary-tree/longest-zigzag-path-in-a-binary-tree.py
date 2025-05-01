# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        longest = 0
        stack = [(root, True, 0), (root, False, 0)]

        while stack:
            node, is_right, count = stack.pop()

            longest = max(longest, count)

            if is_right:
                if node.right:
                    stack.append((node.right, False, count + 1))
                if node.left:
                    stack.append((node.left, True, 1))
            else:
                if node.left:
                    stack.append((node.left, True, count + 1))
                if node.right:
                    stack.append((node.right, False, 1))

        return longest