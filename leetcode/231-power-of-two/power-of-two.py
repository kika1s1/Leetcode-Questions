class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def power_two(n):
            if n == 1:
                return True
            if n == 0 or n % 2 !=0:
                return False
            return power_two(n//2)
        return power_two(n)