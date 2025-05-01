class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        suffix_sums = [0] * n
        suffix_sums[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sums[i] = piles[i] + suffix_sums[i + 1]
        
        @lru_cache(None)
        def dp(i: int, M: int) -> int:
            if i + 2 * M >= n:
                return suffix_sums[i]
            
            max_stones = 0
            for x in range(1, 2 * M + 1):
                next_M = max(M, x)
                opponent_stones = dp(i + x, next_M)
                max_stones = max(max_stones, suffix_sums[i] - opponent_stones)
            
            return max_stones
        
        return dp(0, 1)