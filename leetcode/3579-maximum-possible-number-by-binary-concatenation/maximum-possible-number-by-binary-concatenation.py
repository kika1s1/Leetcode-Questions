class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        maxim = 0
        conc = ""
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i !=j  and j !=k and i !=k:
                        conc +=bin(nums[i])[2:]
                        conc +=bin(nums[j])[2:]
                        conc +=bin(nums[k])[2:]
                        maxim  = max(int(conc, 2), maxim)
                        conc = ""
        
        return maxim
