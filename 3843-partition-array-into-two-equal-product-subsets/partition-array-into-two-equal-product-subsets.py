from math import prod
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        product = 1
        for num in nums:
            product *=num
        if product != target ** 2:
            return False
        def backtrack(sub,  index):
            if prod(sub) == target:
                return True
            if prod(sub) > target:
                return False
            for i in range(index, len(nums)):
                sub.append(nums[i])
                if backtrack(sub, i+1):
                    return True
                sub.pop()
                if backtrack(sub, i+1):
                    return True
            return False
        return backtrack([],  0)
             