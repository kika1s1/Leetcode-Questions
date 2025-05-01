class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(indx, posAns, total):
            if total == target:
                ans.append(posAns[:])
                return 
            if total > target:
                return 
            for i in range(indx, len(candidates)):
                if i != indx and candidates[i] ==candidates[i-1]:
                    continue
                posAns.append(candidates[i])
                backtrack(i+1, posAns, total + candidates[i])
                posAns.pop()

        backtrack(0, [], 0)
        return ans