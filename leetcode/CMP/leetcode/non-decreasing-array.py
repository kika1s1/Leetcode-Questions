class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        streak1 = 0
        streak2 = 0
        n = nums.copy()
        if len(nums) == 1:
            return True
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                nums[i-1] = nums[i]
                break
        for i in range(1, len(n)):
            if n[i-1] > n[i]:
                n[i] = n[i-1]
                break

        for i in range(1, len(n)):
            if n[i-1] > n[i]:
                streak1 += 1
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                streak2 += 1
        if streak1 == 0 or streak2 == 0:
            return True

        return False
        # is_non_decreasing = False
        # for i in range(1, len(nums)):
        #     if nums[i - 1] > nums[i]:
        #         if is_non_decreasing:
        #             return False
        #         is_non_decreasing = True
        #         if i < 2 or nums[i - 2] <= nums[i]:
        #             nums[i - 1] = nums[i]
        #         else:
        #             nums[i] = nums[i - 1]
        # return True

