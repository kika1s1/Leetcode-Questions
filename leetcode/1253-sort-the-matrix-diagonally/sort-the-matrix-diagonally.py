class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        lst = []
        n, m = len(mat), len(mat[0])
        
        for i in range(n):
            lst.append([i, 0])
        
        for i in range(m):
            lst.append([0, i])
        
        lst.pop(0)
        
        for x, y in lst:
            arr = []
            i, j = x, y
            
            while i < n and j < m:
                arr.append(mat[i][j])
                i, j = i+1, j+1
            
            arr.sort() 
            
            i, j = x, y
            while i < n and j < m:
                mat[i][j] = arr.pop(0)
                i, j = i+1, j+1
        
        return mat