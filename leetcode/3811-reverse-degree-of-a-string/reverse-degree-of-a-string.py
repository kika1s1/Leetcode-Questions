class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for index, char in enumerate(s):
            ans +=((ord("z")-ord(char)+1)*(index+1))
        return ans
