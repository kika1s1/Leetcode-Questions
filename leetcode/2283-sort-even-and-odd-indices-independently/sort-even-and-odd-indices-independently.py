class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        eve = []
        for i in range(len(nums)):
            if i % 2 == 0:
                eve.append(nums[i])
                nums[i] = 1
            elif i % 2 == 1:
                odd.append(nums[i])
                nums[i] = 0

        eve.sort(reverse=True)
        odd.sort()

        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i] = eve.pop()
            elif nums[i] == 0:
                nums[i] = odd.pop()

        return nums
                