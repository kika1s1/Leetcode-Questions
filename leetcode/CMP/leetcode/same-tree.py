# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(t,ans):
            if t==None:
                ans.append(None)
                return
            ans.append(t.val)
            preorder(t.left,ans)
            preorder(t.right,ans)
        ans=[]
        ans2=[]
        preorder(p,ans)
        preorder(q,ans2)
        if ans==ans2:
            return True
        else:
            return False
                