class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = [chr(i) for i in range(65, 91)]
        ans = ""
        while columnNumber >= 26:
            if columnNumber % 26 == 0:
                ans = "Z" + ans
                columnNumber -=26
                columnNumber //=26
            else:
                mod = columnNumber%26
                ans = alphabet[mod-1] + ans
                columnNumber -=mod
                columnNumber //=26
        if columnNumber:
            ans = alphabet[columnNumber-1] + ans
        return ans

            
