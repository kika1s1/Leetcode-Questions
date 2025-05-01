class Solution:
    def smallerNumbersThanCurrent(self, nums):
        frequency = [0] * 101
        for n in nums:
            frequency[n] += 1
            
        previousAggregate = 0
        currentAggregate = 0
        for i in range(len(frequency)):
            currentAggregate += frequency[i]
            frequency[i] = previousAggregate
            previousAggregate = currentAggregate
        
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = frequency[nums[i]]
        
        return result