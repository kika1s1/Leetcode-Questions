class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        d = 2
        ans = 1
        while d <= a and d <=b:
            if a%d == 0 and b % d ==0:
                ans = d
            d +=1
        return ans