# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        check = set(stones)
        memo = {}

        def dp(idx, prev):
            if idx == stones[-1]:
                return True
            if idx > stones[-1]:
                return False
                
            if idx not in check:
                return False

            if (idx, prev) not in memo:
                if prev > 1:
                    memo[(idx, prev)] = dp(idx + prev-1, prev-1) or dp(idx + prev, prev)  or dp(idx + prev + 1, prev+1)
                elif prev == -1:
                    memo[(idx, prev)] = dp(idx + 1, 1)
                else:
                    memo[(idx, prev)] = dp(idx + prev, prev)  or dp(idx + prev + 1, prev+1)


            return memo[(idx, prev)]

        return dp(0, -1)
