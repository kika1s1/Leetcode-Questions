class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        K = len(nums)
        ans = []
        def backtrack(curr):
            if len(curr) == K:
                ans.append(curr[:])
                return 
            for num in nums:
                if num in curr:
                    continue
                curr.append(num)
                backtrack(curr)
                curr.pop()
            return ans
        return backtrack([])