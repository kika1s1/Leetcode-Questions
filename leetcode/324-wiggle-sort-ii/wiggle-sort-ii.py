class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        nums.sort(reverse=True)
        nums[1::2], nums[::2] = (nums[:n//2], nums[n//2:])       