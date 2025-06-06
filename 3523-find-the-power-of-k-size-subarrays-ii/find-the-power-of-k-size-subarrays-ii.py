class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # return nums
        cnt_order = [1]
        N = len(nums)
        for i in range(1, N):
            if nums[i] > nums[i-1] and nums[i-1] + 1 == nums[i]:
                cnt_order.append(cnt_order[-1] + 1)
            else:
                cnt_order.append(1)
        ans = []
        for i in range(N-k+1):
            if nums[i] + k-1 == nums[i+k-1] and cnt_order[i+k-1] - cnt_order[i] + 1 ==k:
                ans.append(nums[i+k-1])
            else:
                ans.append(-1)
        return ans

