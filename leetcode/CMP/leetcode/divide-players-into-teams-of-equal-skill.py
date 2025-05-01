class Solution:
    def dividePlayers(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        a = [A[i]+A[n-i-1] for i in range(n//2)]
        if len(set(a)) != 1: return -1
        return sum(A[i]*A[n-i-1] for i in range(n//2)) 