#
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:

        cnt = 0
        n = len(nums)
        for i in range(n):
            current_lcm = nums[i]
            if current_lcm == k:
                cnt += 1
            for j in range(i + 1, n):
                current_lcm = lcm(current_lcm, nums[j])
                if current_lcm > k:
                    break
                if current_lcm == k:
                    cnt += 1
        return cnt
