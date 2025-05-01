class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans =  0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sub = nums[i:j+1]
                if len(sub) > ans:
                    prod = 1
                    for num in sub:
                        prod *=num
                    if prod == lcm(*sub)*gcd(*sub):
                        ans = len(sub)
        return ans