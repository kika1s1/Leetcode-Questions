class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        middle = []
        for num in nums:
            if num > pivot:
                right.append(num)
            elif num == pivot:
                middle.append(num)
            else:
                left.append(num)
        return left + middle + right