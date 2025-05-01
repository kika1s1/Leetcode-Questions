class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node,val):
            if not node:
                return False

            val += chr(ord('a') + node.val)
            left = dfs(node.left , val)
            right = dfs(node.right , val)

            if not left and not right:
                res.append(val[::-1])
            return True
            
        dfs(root,"")
        res.sort()
        return res[0]