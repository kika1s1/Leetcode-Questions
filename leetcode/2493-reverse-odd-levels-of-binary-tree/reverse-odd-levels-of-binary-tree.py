# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = []
        queue = deque([root])
        cnt =  0
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            if level and cnt % 2 ==1:
                result.extend(list(reversed(level)))
            elif level:
                result.extend(level)
            cnt +=1
        def build(index):
            if index >= len(result):  
                return None
            node = TreeNode(result[index])
            node.left = build(2 * index + 1)
            node.right = build(2 * index + 2)
            
            return node
        return build(0)
