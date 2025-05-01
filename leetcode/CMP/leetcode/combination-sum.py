class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(indx, posAns, _sum):
            if _sum == target:
                ans.append(posAns[:])
                return 
            if _sum > target or indx > len(candidates)-1:
                return 
            for i in range(indx, len(candidates)):
                posAns.append(candidates[i])
                backtrack(i, posAns, _sum +candidates[i])
                posAns.pop()
        ans = []
        backtrack(0, [], 0)
        return ans