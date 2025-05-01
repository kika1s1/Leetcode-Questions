class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        results = []
        R, C = len(grid), len(grid[0])
        initial = grid[0][0]
        for i in range(R):
            for j in range(C):
                if abs(initial - grid[i][j]) % x !=0:
                    return -1
                else:
                    results.append(grid[i][j])
        results.sort()
        mid_value = results[len(results)//2]
        times = 0
        for num in results:
            times += abs(num - mid_value) //x
        return times

