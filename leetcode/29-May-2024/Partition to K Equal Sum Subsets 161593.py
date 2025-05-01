# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        target = total // k
        used = [False] * len(nums)
        def backtrack(start, subsets, current_sum):
            if subsets == 0:
                return True
            if current_sum == target:
                return backtrack(0, subsets - 1, 0)

            for i in range(start, len(nums)):
                if used[i] or current_sum + nums[i] > target:
                    continue

                used[i] = True

                if backtrack(i + 1, subsets, current_sum + nums[i]):
                    return True

                used[i] = False

                if current_sum == 0:
                    return False

            return False

        return backtrack(0, k, 0)