class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        ans = -1
        repHash = Counter(arr)
        for i, j in repHash.items():
            if i == j:
                ans = max(ans, i)
        return ans