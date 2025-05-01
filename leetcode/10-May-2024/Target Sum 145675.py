# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        memo = {}
        def backtrack(index, curr_sum):
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]
            
            if index == N:
                if curr_sum == target:
                    return 1
                else:
                    return 0
            
            pos = backtrack(index + 1, curr_sum + nums[index])
            neg = backtrack(index + 1, curr_sum - nums[index])
            memo[(index, curr_sum)] = pos + neg
            return memo[(index, curr_sum)]
        
        return backtrack(0, 0)


# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         N = len(nums)
#         cnt = 0
#         def backtrack(nums, index, current):
#             nonlocal cnt
#             if index == N:
#                 if sum(current) == target:
#                     cnt += 1
#                     print(current)
#                 return
            
#             current.append(nums[index])
#             backtrack(nums, index + 1, current)
#             current.pop()
            
#             current.append(-nums[index])
#             backtrack(nums, index + 1, current)
#             current.pop()
        
#         backtrack(nums, 0, [])
#         return cnt