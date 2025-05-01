class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        best = -1

        while left <= right:
            mid = left + (right - left) // 2

            hours = 0
            for pile in piles:
                hours += (pile - 1) // mid + 1

            if hours > h:
                left = mid + 1
            else:
                right = mid - 1
                best = mid

        return best