class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = {2,3,5}
        seen = {1}
        heap = [1]
        for i in range(n-1):
            mul = heappop(heap)
            for num in primes:
                if mul * num not in  seen:
                    heappush(heap, mul*num)
                    seen.add(mul*num)
        return heappop(heap)