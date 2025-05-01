class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        see = False
        for char in s:
            if not ans:
                ans +=char
            elif ans and ans[-1] != char:
                ans +=char
                see = False
            elif ans and ans[-1] == char and not see:
                see = True
                ans +=char
            else:
                continue
            

        return ans