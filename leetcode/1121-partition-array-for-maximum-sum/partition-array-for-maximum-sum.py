class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):
            max_elm = -1
            max_score = -1
            segment_len = 0

            for j in range(i,min(i+k,n)):
                segment_len += 1
                max_elm = max(max_elm,arr[j])
                score = segment_len*max_elm + dp[j+1]
                max_score = max(max_score,score)
            dp[i] = max_score

        return dp[0]