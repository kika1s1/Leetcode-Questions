class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        N = len(nums)
        cnt = 0
        for i in range(N):
            for j in range(N):
                if i !=j:
                    sub = nums[i] + nums[j]
                    if sub == target:
                        cnt +=1
        return cnt