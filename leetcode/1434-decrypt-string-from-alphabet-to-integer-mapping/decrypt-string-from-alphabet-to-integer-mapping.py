class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        skip = 0
        
        for i in range(len(s)-1, -1, -1):
            if skip > 0:
                skip -= 1
                continue
            
            if s[i] == '#':
                res += chr(int(s[i-2:i]) + 96)
                skip = 2
            else:
                res += chr(int(s[i]) + 96)
        
        return res[::-1]