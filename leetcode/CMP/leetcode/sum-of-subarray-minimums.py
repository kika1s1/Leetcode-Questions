class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        A = [-inf] + arr + [-inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res % 1000000007