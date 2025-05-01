class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        if k*2 >= len(nums):
            return [-1]*len(nums)
        ans = []
        for i in range(k):
            ans.append(-1)

        l = k*2

        loop = (len(nums) - (k*2))
        total = sum(nums[0:((k*2)+1)])
        ans.append(total//(k*2+1))
        for i in range(loop-1):
            l += 1
            total += nums[l] - nums[i]
            ans.append(total//(k*2+1))

        for i in range(len(nums)-len(ans)):
            ans.append(-1)
        return ans