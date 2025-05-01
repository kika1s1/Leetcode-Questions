class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1
        prev = [float('inf')] * n
        curr = [float('inf')] * n
        for day in range(d):
            stack = []
            for i in range(day, n):
                if i == 0:
                    curr[i] = jobDifficulty[0]
                else:
                    curr[i] = prev[i - 1] + jobDifficulty[i]
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:
                    j = stack.pop()
                    curr[i] = min(curr[i], curr[j] + jobDifficulty[i] - jobDifficulty[j])
                if stack:
                    curr[i] = min(curr[i], curr[stack[-1]])
                stack.append(i)
            prev, curr = curr, prev
        return prev[-1]