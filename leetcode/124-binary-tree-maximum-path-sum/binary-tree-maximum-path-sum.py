class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxim = float("-inf")
        
        def dfs(node):
            nonlocal maxim
            if not node:
                return 0
            
            left_gain = max(dfs(node.left), 0)  
            right_gain = max(dfs(node.right), 0)
            current_max = node.val + left_gain + right_gain
            maxim = max(maxim, current_max)
            return node.val + max(left_gain, right_gain)
        dfs(root)
        return maxim