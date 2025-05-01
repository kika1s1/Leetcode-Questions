# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        data =defaultdict(int)
        def dfs(root):
            if root:
                dfs(root.left)
                data[root.val] +=1
                dfs(root.right)
        dfs(root)
        dataList = list(data.items())
        # print(dataList)
        dataList.sort(key=lambda x: x[1], reverse=True)
        items = []
        for i in range(len(dataList)):
            if dataList[0][1] == dataList[i][1]:
                items.append(dataList[i][0])
        return items