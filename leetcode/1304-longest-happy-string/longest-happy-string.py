import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        result = []
        
        while heap:
            count1, char1 = heapq.heappop(heap)
            
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not heap:
                    break  
                count2, char2 = heapq.heappop(heap)
                result.append(char2)
                if count2 + 1 < 0:
                    heapq.heappush(heap, (count2 + 1, char2))  
                heapq.heappush(heap, (count1, char1))
            else:
                result.append(char1)
                if count1 + 1 < 0:
                    heapq.heappush(heap, (count1 + 1, char1))  
        return ''.join(result)