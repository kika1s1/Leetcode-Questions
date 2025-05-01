class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        ans = 0
        for i in range(len(nums) - 1):
            if prefix[i + 1] >= prefix[-1] - prefix[i + 1]:
                ans += 1
        
        return ans
