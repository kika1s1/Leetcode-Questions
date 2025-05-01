class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        elementIdx = {}
        for i, v in enumerate(elements):
            if v not in elementIdx:
                elementIdx[v] = i
        
        n = len(groups)
        assigned = [-1] * n

        for i in range(n):
            root = int(groups[i] ** 0.5) + 1
            idx = float('inf')
            for x in range(1, root):
                if groups[i] % x == 0:
                    num = groups[i] // x
                    if x in elementIdx:
                        idx = min(idx, elementIdx[x])
                    if num in elementIdx:
                        idx = min(idx,  elementIdx[num])
            if idx != float('inf'):
                assigned[i] = idx
        return assigned