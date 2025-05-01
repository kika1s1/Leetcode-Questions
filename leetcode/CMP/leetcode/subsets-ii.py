class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start, sub, ans, nums):
            ans.append(sub[:])
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue  
                sub.append(nums[i])
                backtrack(i+1, sub, ans, nums)
                sub.pop()
        ans = []
        nums.sort()
        backtrack(0, [], ans, nums)
        return ans