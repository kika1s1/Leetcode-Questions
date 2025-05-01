class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for j in range(k):
            index = 0
            for k in range(len(nums)):
                if nums[k] < nums[index]:
                    index = k
            nums[index] = multiplier * nums[index]
        return nums
