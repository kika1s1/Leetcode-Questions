class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        ones = nums.count(1)
        l = 0
        cnt_one = max_cnt_one = 0
        for r in range(2*N):
            if nums[r%N]:
                cnt_one +=1
            if r -l+1> ones:
                cnt_one -=nums[l%N]
                l +=1
            max_cnt_one = max(max_cnt_one, cnt_one)
        return ones - max_cnt_one
        