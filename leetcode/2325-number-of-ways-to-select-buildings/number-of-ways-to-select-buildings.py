class Solution:
    def numberOfWays(self, s: str) -> int:
        ways = 0
        one = zero = zero_one = one_zero = 0
        for c in s:
            if c == '0':
                zero += 1
                one_zero += one
                ways += zero_one
            else:
                one += 1    
                zero_one += zero 
                ways += one_zero
        return ways