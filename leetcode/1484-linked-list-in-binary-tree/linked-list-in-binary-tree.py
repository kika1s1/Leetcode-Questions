# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def compare(head, root):
            if not head: 
                return True
            if not root: 
                return False
            if head.val != root.val:  
                return False
            return compare(head.next, root.left) or compare(head.next, root.right)

        def dfs(root):
            if not root:
                return False
            if compare(head, root):
                return True
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)
