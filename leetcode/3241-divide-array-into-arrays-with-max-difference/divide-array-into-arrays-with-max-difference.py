class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        l, r = 0, 2
        while r < len(nums):
            if nums[r]-nums[l] > k:
                return []
            l += 3
            r += 3
        ans = []
        ws = k
        l, r = 0, 3
        while r < len(nums)+1:
            sub = nums[l:r]
            ans.append(sub)
            l = r
            r += 3
        return ans