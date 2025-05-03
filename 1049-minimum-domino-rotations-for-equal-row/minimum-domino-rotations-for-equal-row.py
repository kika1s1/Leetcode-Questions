class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = float("inf")
        for i in range(1, 7):
            # top
            top = 0
            for a, b in zip(tops, bottoms):
                if i == a:
                    continue
                elif b == i:
                    top +=1
                else:
                    top = float("inf")
                    break
            # bottom
            bottom = 0
            for a, b in zip(tops, bottoms):
                if i == b:
                    continue
                elif i == a:
                    bottom += 1
                else:
                    bottom = float("inf")
                    break
            ans = min(ans, top, bottom)
        if ans == float("inf"):
            return -1
        return ans