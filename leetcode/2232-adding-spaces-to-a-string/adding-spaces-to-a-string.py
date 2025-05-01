class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        j = 0
        for index, char in enumerate(s):
            if j < len(spaces) and  index == spaces[j]:
                ans.append(" ")
                ans.append(char)
                j +=1
            else:
                ans.append(char)
        return "".join(ans)