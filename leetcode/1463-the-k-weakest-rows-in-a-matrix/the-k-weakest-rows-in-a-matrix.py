class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        for i, row in enumerate(mat):
            arr.append((i, sum(row)))
        ans = []
        arr.sort(key=lambda x: x[1])
        for i in range(k):
            ans.append(arr[i][0])
        return ans
