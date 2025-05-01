class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f = [1, 1]
        while f[-1] < k:
            f.append(f[-1] + f[-2])
        ans, i = 0, len(f) - 1
        while k:
            if k >= f[i]:
                k -= f[i]
                ans += 1
            i -= 1
        return ans