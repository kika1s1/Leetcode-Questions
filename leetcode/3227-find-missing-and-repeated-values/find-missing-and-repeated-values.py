class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        c = Counter(x for r in grid for x in r)
        d = {c[i]: i for i in range(1, len(grid) ** 2 + 1)}
        return [d[2], d[0]]