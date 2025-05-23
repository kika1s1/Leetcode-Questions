class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(open, close, op, ans):
            if open == 0 and close == 0:
                ans.append(op)
                return 
            if open != 0:
                solve(open - 1, close, op + '(', ans)
            if close > open:
                solve(open, close - 1, op + ')', ans)

        ans = []  
        op = ""   

        solve(n, n, op, ans)
        return ans  

        