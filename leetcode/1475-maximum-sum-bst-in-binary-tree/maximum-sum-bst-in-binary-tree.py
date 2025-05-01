# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def is_valid_bst(node):
            nonlocal max_sum
            if not node:
                return True, float('inf'), float('-inf'), 0

            left_valid, left_min, left_max, left_sum = is_valid_bst(node.left)
            right_valid, right_min, right_max, right_sum = is_valid_bst(node.right)

            if (
                left_valid and right_valid and
                left_max < node.val < right_min
            ):
                current_sum = node.val + left_sum + right_sum
                max_sum = max(max_sum, current_sum)
                return (
                    True,
                    min(left_min, node.val),
                    max(right_max, node.val),
                    current_sum
                )

            return False, float('-inf'), float('inf'), 0

        is_valid_bst(root)
        return max_sum