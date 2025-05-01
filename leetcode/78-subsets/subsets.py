class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(i, curr):
            result.append(curr[:])
            for i in range(i, len(nums)):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()



        backtrack(0, [])
        return result