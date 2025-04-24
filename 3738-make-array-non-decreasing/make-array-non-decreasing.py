class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        prev = nums[0]
        cnt = 0
        for num in nums:
            if prev <= num:
                prev = num
                cnt +=1
        return cnt