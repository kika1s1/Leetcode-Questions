# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         cols_martix = []
#         for i in range(len(grid[0])):
#             sub = [] 
#             for j in range(len(grid)):
#                 sub.append(grid[j][i])
#             cols_martix.append(sub)
#         cnt = 0
#         for i in grid:
#             if i in cols_martix:
#                 cnt +=1

#         return cnt
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = {}
        result = 0
        
        for i in range(len(grid)):
            if tuple(grid[i]) not in count:
                count[tuple(grid[i])] = 1
            elif tuple(grid[i]) in count:
                count[tuple(grid[i])] += 1
        
        for n in range(len(grid)):
            col = [i[n] for i in grid]
            if col in grid:
                result += count[tuple(col)]
        return result
        
        