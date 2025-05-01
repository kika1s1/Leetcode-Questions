class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        best = -1
        while left<=right:
            mid = left+(right-left)//2
            sum = 0
            for ele in nums:
                sum += ceil(ele/mid)
            if sum <= threshold:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best