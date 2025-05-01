class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        tot = 0
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i-1] !=nums[i]:
                cnt +=1
            else:
                tot +=(cnt*(cnt+1))//2
                cnt = 1
        return ((cnt*(cnt+1))//2) + tot