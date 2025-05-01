class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        0,1,7,4,4,5
        0, 1 4  4 5 7
        0  1 2  3 4  5
        0, 4
        0 = 3
        1 = 3
        4 = 0, 0
        """
        ans = 0
        
        nums.sort()
        N  = len(nums)
        for index in range(N):
            left = nums[index]
            maxim = 0
            l = index + 1
            left_index = bisect_left(nums, lower-left, index+1, N)
            right_index = bisect_right(nums, upper-left, index + 1, N)
            ans +=max(0, right_index- left_index)
        return ans