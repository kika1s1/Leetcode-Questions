class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
        heap = [1]
        seen = {1}
        for _ in range(n - 1):
            num = heapq.heappop(heap)
            for prime in primes:
                if num * prime not in seen:
                    seen.add(num * prime)
                    heapq.heappush(heap, num * prime)
        return heapq.heappop(heap)