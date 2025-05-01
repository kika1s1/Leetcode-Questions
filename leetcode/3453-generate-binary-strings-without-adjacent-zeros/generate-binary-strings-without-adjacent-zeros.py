class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []
        def backtrack(cand):
            if len(cand) >= 2 and cand[-1] == "0" and cand[-2] == "0":
                return 
            if len(cand) == n:
                result.append("".join(cand))
                return 
            cand.append("0")
            backtrack(cand)
            cand.pop()
            cand.append("1")
            backtrack(cand)
            cand.pop()
        backtrack([])
        return result