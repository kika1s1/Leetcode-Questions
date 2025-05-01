# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        queue = deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level:
                pos = {x:i for i, x in enumerate(level)}
                sorted_level = sorted(level)
                if sorted_level == level:
                    continue
                else:
                    for index, (a, b) in enumerate(zip(sorted_level, level)):
                        if a == b:
                            continue
                        else:
                            level[pos[a]],level[pos[b]] = level[pos[b]],level[pos[a]]
                            pos[a], pos[b] = pos[b], pos[a]
                            ans +=1

        return ans

    