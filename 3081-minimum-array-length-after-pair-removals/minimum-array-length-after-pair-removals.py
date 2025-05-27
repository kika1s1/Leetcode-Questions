class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        heap = []
        f = Counter(nums)
        for key, value in f.items():
            heappush(heap, (-value, key))
        while heap:
            value, key = heappop(heap)
            if not heap:
                return abs(value)
            val1, key1 = heappop(heap)
            value +=1
            val1 +=1
            if val1:
                heappush(heap, (val1, key1))
            if value:
                heappush(heap, (value, key))
        return 0

