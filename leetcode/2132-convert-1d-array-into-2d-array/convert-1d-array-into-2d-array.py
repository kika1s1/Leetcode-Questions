class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        N = len(original)
        if m*n !=N:
            return []
        ans = []
        for i in range(0, N, n):
            row = original[i:n+i]
            ans.append(row)
        return ans
        
