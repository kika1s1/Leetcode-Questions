class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            A = nums[i]
            B = nums[i+1]
            C = nums[i+2]
            if B+C > A:
                return A+B+C
        return 0