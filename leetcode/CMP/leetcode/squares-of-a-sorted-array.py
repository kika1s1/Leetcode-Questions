class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l]**2 > nums[r]**2:
                ans.append(nums[l]**2)
                l +=1
            else:
                ans.append(nums[r]**2)
                r -=1
        ans.reverse()
        return ans