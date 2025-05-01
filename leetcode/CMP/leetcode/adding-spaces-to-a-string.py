class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        mapWithIndex = {}
        for i in spaces:
            mapWithIndex[i] = s[i]

        for i, j in enumerate(s):
            if i in mapWithIndex:
                ans += " "+j
            else:
                ans += j

        return ans
