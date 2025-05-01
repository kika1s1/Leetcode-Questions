# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        maxim = max(nums)
        node = TreeNode(maxim)
        indx = nums.index(maxim)
        node.left = self.constructMaximumBinaryTree(nums[:indx])
        node.right = self.constructMaximumBinaryTree(nums[indx+1:])
        return node
        