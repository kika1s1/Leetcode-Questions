class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def possible(candies, mid):
            cnt = 0
            for candie in candies:
                cnt +=(candie//mid)
            return cnt >=k

        l, r = 1, max(candies)
        while l <=r:
            mid = (l+r)//2
            if possible(candies, mid):
                l = mid+1
            else:
                r = mid-1
        return l-1