class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        idx_2 = 1
        for idx_1 in range(0, len(nums), 2):
            if nums[idx_1] % 2 != 0:
                while nums[idx_2] % 2 != 0:
                    idx_2 += 2
                nums[idx_1], nums[idx_2] = nums[idx_2], nums[idx_1]
        return nums