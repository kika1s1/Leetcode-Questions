class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def improvement(passed, total):
            return (passed + 1) / (total + 1) - passed / total
        
        heap = []
        for passed, total in classes:
            heapq.heappush(heap, (-improvement(passed, total), passed, total))
        
        for _ in range(extraStudents):
            imp, passed, total = heapq.heappop(heap)
            passed += 1
            total += 1
            heapq.heappush(heap, (-improvement(passed, total), passed, total))
        
        return sum(passed / total for _, passed, total in heap) / len(classes)
