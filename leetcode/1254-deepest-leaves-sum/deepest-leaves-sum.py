# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        l=defaultdict(list)
        def dls(node,h):
            if node is None:
                return
            l[h].append(node.val)
            dls(node.left,h+1)
            dls(node.right,h+1)
        dls(root,0)
        return sum(l[len(l)-1])