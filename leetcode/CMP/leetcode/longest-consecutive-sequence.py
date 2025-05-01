class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = list(set(nums))
        # nums.sort()
        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return 1

        # longest = 0
        # cnt = 1
        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i-1] == 1:
        #         cnt += 1
        #     else:

        #         cnt = 1
        #     longest = max(cnt, longest)
        # return longest
        s = set(nums)
        left = 0
        right = 0

        max_length = 0
        for num in nums:
            if left < num < right:
                continue
                
            tmp = num
            length = 0
            while tmp in s:
                length += 1
                tmp -=1
            
            if length > max_length:
                max_length = length
                left = tmp + 1
                right = left + length

            tmp = num
            length = 0
            while tmp in s:
                length += 1
                tmp +=1
            if length > max_length:
                max_length = length
                right = tmp - 1
                left = right - length

        return max_length
