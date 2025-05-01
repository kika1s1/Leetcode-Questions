class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        count = 0
        min_pos = max_pos = bad_pos = -1
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                bad_pos = i
            if nums[i] == minK:
                min_pos = i
            if nums[i] == maxK:
                max_pos = i
            
            count += max(0, min(min_pos, max_pos) - bad_pos)
            # print(count)
        return count