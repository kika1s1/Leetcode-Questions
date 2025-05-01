class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset, ans):
            ans.append(subset[:])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset, ans)
                subset.pop()
        
        ans = []
        backtrack(0, [], ans)
        return ans
