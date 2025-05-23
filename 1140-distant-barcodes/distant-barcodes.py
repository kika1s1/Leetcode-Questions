class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        bar_rep  = Counter(barcodes)
        heap = []
        for key, value in bar_rep.items():
            heappush(heap, (-value, key))
        ans = deque()
        while heap:
            value, key = heappop(heap)
            ans.append(key)
            if heap:
                left_val, key_val = heappop(heap)
                ans.append(key_val)
                left_val +=1
                if left_val != 0:
                    heappush(heap, (left_val, key_val))
            value +=1

            if value != 0:
                heappush(heap, (value, key))
        return list(ans)

            