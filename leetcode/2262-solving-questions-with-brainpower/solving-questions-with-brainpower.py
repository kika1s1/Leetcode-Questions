class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """

        [[3,2],[4,3],[4,4],[2,5]]
        0      1      2     3
        3 ,2 |   4, 3  | 4, 4, | 2, 5
        create ans = [0]* len(questions)
        start from end and continue adding
        how to add:
            add 4 and nth together 
        return maxim
        """
        N = len(questions)
        dp = [0]*(N+1)
        for i in range(N-1,-1,-1):
            points, brainpower = questions[i]
            take=points
            if i + brainpower+1< N:
                take += dp[i + brainpower+1]
            skip = dp[i+1]
            dp[i] = max(take, skip)
        return dp[0]
