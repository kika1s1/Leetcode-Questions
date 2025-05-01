class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        total = 0
        N = len(nums)
        for index in range(N):
            below = index - k
            above = index + k
            if 0 <=above<N and 0 <=below < N:
                if nums[below] < nums[index] and nums[above] < nums[index]:
                    total +=  nums[index]
            elif 0 <=below<N:
                if nums[below] < nums[index]:
                    total +=nums[index]
            elif 0 <=above<N:
                if nums[above] < nums[index]:
                    total +=nums[index]
        return total

