# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashTable = {}
        def traverse(root, col, row):
            if root is None:
                return 
            if col not in hashTable:
                hashTable[col] =[(row, root.val)]
            else:
                hashTable[col].append((row, root.val))
            if root.left is not None:
                traverse(root.left, col-1, row+1)
            if root.right is not None:
                traverse(root.right, col+1, row+1)
        traverse(root, 0, 0)
        print(hashTable)
        index = list(hashTable)
        value = [x for x in hashTable.values()]
        for i in range(len(index)):
            for j in range(len(index)-i-1):
                if index[j] > index[j+1]:
                    index[j], index[j+1] =  index[j+1], index[j]
                    value[j], value[j+1] = value[j+1], value[j]
        # for i in value:
        # #     i.sort()
        for item in value:
            item.sort()
        ans = []
        for item in value:
            val = []
            for dum in item:
                val.append(dum[1])
            ans.append(val)

                
        return ans