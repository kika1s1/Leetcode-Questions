class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def backtrack(target):
            if target in memo:
                return memo[target]
            
            if target == 0:
                return 1
            
            count = 0
            for num in nums:
                if target >= num:
                    count += backtrack(target - num)
            
            memo[target] = count
            return count
        
        return backtrack(target)