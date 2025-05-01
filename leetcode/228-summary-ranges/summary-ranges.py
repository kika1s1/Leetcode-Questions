class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        N = len(nums)
        if not nums:
            return result
        start = nums[0]

        for i in range(1, N + 1):
            if i == N or nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                if i < N:
                    start = nums[i]
        return result
