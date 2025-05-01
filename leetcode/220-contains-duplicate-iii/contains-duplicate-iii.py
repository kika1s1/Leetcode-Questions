from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        order = SortedList()
        for index, num in enumerate(nums):
            if index > indexDiff:
                order.remove(nums[index - indexDiff - 1])
            pos = order.bisect_left(num - valueDiff)
            if pos < len(order) and abs(order[pos] - num) <= valueDiff:
                return True
            order.add(num)          
        return False

