class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            sep = []
            while num > 9:
                rem = num %10
                sep.append(rem)
                num //=10
            sep.append(num)
            ans.extend(sep[::-1])
        return ans


