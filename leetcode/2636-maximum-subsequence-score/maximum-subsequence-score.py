
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = 0
        total_sum = 0 
        heap = [] 
       
        merged = [(nums2[i], nums1[i]) for i in range(len(nums1))]
        merged.sort(reverse=True)

        for maxOf2, num1Val in merged: 
            if len(heap) == k: 
                total_sum -= heapq.heappop(heap)  

            total_sum += num1Val
            heapq.heappush(heap, num1Val)  
           
            if len(heap) == k:
                result = max(result, total_sum * maxOf2) 
        return result