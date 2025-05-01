class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}
        for i, j in enumerate(nums):
            if j in hashNum:
                return [i, hashNum[j]]
            else:
                hashNum[target-j] = i
            
        