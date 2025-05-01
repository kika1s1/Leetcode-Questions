class Solution:
    def isCovered(self, matrix: List[List[int]], l: int, r: int) -> bool:
        mat = []
        
        for start, end in matrix:
            mat.extend(list(range(start, end + 1)))
        
        for i in range(l, r + 1):
            if i not in mat:
                return False
        
        return True