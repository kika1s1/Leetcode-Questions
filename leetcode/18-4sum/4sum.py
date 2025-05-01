from typing import List
from collections import defaultdict

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(set(nums)) == 1 and len(nums) >=4:
            return [nums[:4]] if sum(nums[:4]) == target else []
        nums.sort()  
        pair_sums = defaultdict(list)
        n = len(nums)
        result = set() 
        for i in range(n):
            for j in range(i + 1, n):
                pair_sum = nums[i] + nums[j]
                pair_sums[pair_sum].append((i, j))

        for i in range(n):
            for j in range(i + 1, n):
                current_sum = nums[i] + nums[j]
                complement = target - current_sum
                if complement in pair_sums:
                    for (k, l) in pair_sums[complement]:
                        if k > j:
                            quad = (nums[i], nums[j], nums[k], nums[l])
                            result.add(tuple(sorted(quad)))

        return [list(quad) for quad in result]
