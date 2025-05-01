class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        degree = [0] * n

        for a, b in roads:
            degree[a] += 1
            degree[b] += 1

        degree.sort()

        return sum(i * d for i, d in enumerate(degree, 1))