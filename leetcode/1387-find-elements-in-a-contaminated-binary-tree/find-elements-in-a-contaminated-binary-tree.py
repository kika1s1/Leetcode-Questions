# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    

    def __init__(self, root: Optional[TreeNode]):
        self.exist = set([0])
        root.val = 0
        def dfs(root, cnt):
            if root:
                if root.left:
                    root.left.val = 2*cnt +1
                    self.exist.add(2*cnt +1)

                    dfs(root.left, 2*cnt +1)

                if root.right:
                    root.right.val = 2 * cnt + 2
                    self.exist.add(2 * cnt + 2)
                    dfs(root.right, 2 * cnt + 2)
            

        dfs(root, 0)

        

    def find(self, target: int) -> bool:
        if target in self.exist:
            return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)