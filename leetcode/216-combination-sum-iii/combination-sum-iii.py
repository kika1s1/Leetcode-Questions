class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(i, start, sm, path):
            if i == k and sm == n:
                res.append(path[:])
                return

            for j in range(start, 10):
                if sm + j <= n:
                    path.append(j)
                    backtrack(i + 1, j + 1, sm + j, path)
                    path.pop()
                else:
                    break
        res = []
        backtrack(0, 1, 0, [])
        return res
