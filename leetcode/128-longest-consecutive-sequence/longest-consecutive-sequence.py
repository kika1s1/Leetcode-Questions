class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for n in num_set:
            if (n-1) not in num_set:
                length = 0
                while n in num_set:
                    n +=1
                    length +=1
                longest = max(longest, length)
        
        return longest