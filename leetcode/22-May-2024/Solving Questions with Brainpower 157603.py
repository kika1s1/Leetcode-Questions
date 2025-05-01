# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        best=[0]*(n+1)
        @cache
        def go(i):
            if i>=n:
                return 0

            best=0
            best=max(go(i+1),best)
            best=max(go(i+questions[i][1]+1)+questions[i][0],best)
            return best


        return go(0)      