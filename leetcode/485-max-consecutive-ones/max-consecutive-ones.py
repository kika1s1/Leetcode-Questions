class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxim = float("-inf")
        cnt = 0
        for i in nums:
            if i == 1:
                cnt +=1
                maxim = max(maxim, cnt)
            else:
                # maxim = max(maxim, cnt)
                cnt = 0
        return 0 if maxim == float("-inf") else maxim