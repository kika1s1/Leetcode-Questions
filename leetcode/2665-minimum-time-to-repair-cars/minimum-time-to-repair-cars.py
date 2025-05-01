class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        def possible(ranks, time):
            maxim = float("-inf")
            total_cars = 0
            for rank in ranks:
                total_cars += int(sqrt(time/rank))
            return total_cars >= cars
        l, r = 1, max(ranks) *(cars**2)
        best  =  r
        while l <=r:
            mid = (l+r)//2
            if possible(ranks, mid):
                best = mid
                r = mid -1
            else:
                l = mid +1
        return best