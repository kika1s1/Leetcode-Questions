class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(index, curr, target):
            if sum(curr) == target and sorted(curr) not in ans:
                ans.append(sorted(curr[:]))
                return 
            if sum(curr) > target:
                return 
            for i in range(index, len(candidates)):
                curr.append(candidates[i])
                backtrack(index, curr, target)
                curr.pop()
            return ans
        return backtrack(0, [], target)