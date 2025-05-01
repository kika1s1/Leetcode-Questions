class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        total = 0
        cnt = 0
        for i in range(1, n+1):
            if i not in banned:
                cnt +=1
                total +=i
            if total > maxSum:
                return cnt-1
        return cnt
