class Solution:
    def getMaximumXor(self, nums, maximumBit):
        k = 2 ** maximumBit - 1
        prefix = [nums[0]]
        n = len(nums)

        for i in range(1, n):
            prefix.append(prefix[i - 1] ^ nums[i])

        ans = []
        
        for i in range(n - 1, -1, -1):
            ans.append(prefix[i] ^ k)

        return ans
