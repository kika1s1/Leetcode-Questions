class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        nodeToNext = {node: [] for node in range(n)}
        nodeToPrev = {node: 0 for node in range(n)}
        for prev, nextt in relations:
            nodeToNext[prev-1].append(nextt-1)
            nodeToPrev[nextt-1] += 1
        
        heap = []
        for node, prevCnt in nodeToPrev.items():
            if prevCnt == 0:
                heappush(heap, (time[node], node))
        
        while heap:
            tm, node = heappop(heap)
            for nextt in nodeToNext[node]:
                nodeToPrev[nextt] -= 1
                if nodeToPrev[nextt] == 0:
                    heappush(heap, (tm + time[nextt], nextt))
        
        return tm