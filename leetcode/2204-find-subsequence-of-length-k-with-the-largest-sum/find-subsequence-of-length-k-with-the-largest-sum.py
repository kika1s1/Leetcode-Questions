class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ordered = sorted(nums)
        last =Counter(ordered[-k:])
        ans = []
        for num in nums:
            if num in last and last[num] >0:
                ans.append(num)
                last[num] -=1
        return ans

