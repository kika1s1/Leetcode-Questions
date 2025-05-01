class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def count(n,ans):
            if n==0:
                return ans+1
            ans += 9*factorial(9)//factorial(10-n)
            return count(n-1,ans)
        return count(n,0)