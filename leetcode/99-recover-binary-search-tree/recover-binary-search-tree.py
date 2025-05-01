# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root)
            inorder(root.right)
        arr=[]
        inorder(root)
        new_arr=sorted(arr,key=lambda x: x.val)
        for i in range(len(arr)):
            if arr[i]!=new_arr[i]:
                arr[i].val, new_arr[i].val=new_arr[i].val, arr[i].val
                break
        return root
        
            
        