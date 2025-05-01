class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        N = len(nums)
        if value == 1:
            return N
        for i, num in enumerate(nums):
            nums[i] %=value
        numbers = set()
        for num in nums:
            if num in numbers:
                while num  in numbers:
                    num +=value
            numbers.add(num)
        for i, num in enumerate(sorted(list(numbers))):
            if i !=num:
                return i
        return i+1
        