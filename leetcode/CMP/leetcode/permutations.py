class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perm, perms, nums):
            if len(perm) == len(nums):
                perms.append(perm[:])
                return 
            for num in nums:
                if num not in perm:
                    perm.append(num)
                    backtrack(perm, perms, nums)
                    perm.pop() 
        perms = []
        backtrack([], perms, nums)
        return perms