class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        cnt = defaultdict(int)
        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                heappush(heap, (-grid[i][j], i))
        ans = 0
        while k > 0:
            val, row = heappop(heap)
            if limits[row] > cnt[row]:
                ans +=abs(val)
                k -=1
                cnt[row] +=1
        return ans
